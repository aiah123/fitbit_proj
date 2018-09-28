import datetime
import json
import traceback
import pandas as pd

from src.database.FitibitDatabaseUpdateManager import *
from src.util_funcs import get_date_from_string, log, create_db_file_name


class FitbitDatabaseWriter:

    def __init__(self, db_sections, db_path, first_data_date, log_file_name):
        self.first_data_date = first_data_date
        self.database_path = db_path
        self.log_file_name = log_file_name
        self.update_manager = FitbitDatabaseUpdateManager(db_path, db_sections)
        self.update_manager.handle_db_update_status_file()

    def update_section(self, section_config):

        last_update = self.update_manager.get_last_update_date(section_config.update_file_param_name)

        last_update = get_date_from_string(last_update)
        day_delta = datetime.timedelta(days=1)
        today = datetime.datetime.today().date()  # .strftime('%Y-%m-%d')
        if last_update < self.first_data_date:
            start_date = self.first_data_date
        elif last_update == today:
            log('Database is already up to date', self.log_file_name)
            start_date = None
        else:
            start_date = last_update + day_delta
        current_date = start_date
        if start_date is None:
            return False
        else:
            self.__get_new_data(current_date, day_delta, section_config, today)
            return True

    def __get_new_data(self, current_date, day_delta, section_config, today):
        fitbit_api = section_config.api_call_class
        update_section_name = section_config.update_file_param_name
        folder = section_config.db_folder
        file_prefix = section_config.db_file_prefix

        while current_date <= today:
            file_name = create_db_file_name(self.database_path, current_date, file_prefix, folder)
            try:
                self.__write_json_file_to_database(current_date, fitbit_api, file_name)
            except Exception as e:
                self.write_file_exception(e, file_name, self.log_file_name)
                os.remove(file_name)
                raise ValueError(e)

            try:
                self.__create_pickle_file(file_name, fitbit_api)
            except Exception as e:
                self.write_file_exception(e, self.get_pickle_file_name(file_name), self.log_file_name)
                os.remove(file_name)
                os.remove(self.get_pickle_file_name(file_name))
                raise ValueError(e)

            # the date written to the update status log is yesterday. This is to prevent a case where only
            # part of a date is loaded to the db but the status of that day will be 'updated'
            self.update_manager.set_last_update(str(current_date - datetime.timedelta(days=1)), update_section_name)
            current_date = current_date + day_delta

    def write_file_exception(self, e, file_name, log_name):
        log('Could not write file to database: ' + file_name + '\n' + str(e), log_name)
        log(traceback.print_exc(), log_name)

    def __write_json_file_to_database(self, current_date, fitbit_api, file_name):
        response = fitbit_api.get_data(current_date, '00:00', '23:59')

        if os.path.exists(file_name):
            os.remove(file_name)
        with open(file_name, "a") as f:
            f.write(str(response.content.decode("utf-8")))
        log('Wrote file to database: ' + file_name, self.log_file_name)

    def __create_pickle_file(self, json_file_name, api):

        # get json db file
        with open(json_file_name) as f:
            json_obj = json.load(f)
        date = api.get_date_from_json(json_obj)
        data_list = api.get_data_from_json(json_obj)
        daily_dict = {datetime.datetime.strptime(date + x[api.get_time_key_name()],
                                                 api.get_series_date_format()):
                          [x[value] for value in api.get_values_names()] for x in data_list}  # Mati

        # make dataFrmae
        df = pd.DataFrame.from_dict(daily_dict, orient='index', columns=api.get_columns())

        # write pickle from the dataFrame
        pickle_file_name = self.get_pickle_file_name(json_file_name)
        if os.path.exists(pickle_file_name):
            os.remove(pickle_file_name)

        df.to_pickle(pickle_file_name)
        log('Wrote file to database: ' + pickle_file_name, self.log_file_name)


    def get_pickle_file_name(self, json_file_name):
        dot_location = json_file_name.rfind('.')
        pickle_file_name = json_file_name[:dot_location + 1] + 'pkl'
        return pickle_file_name
