import configparser
import os

LAST_UPDATE_PARAM = 'last_update'
never_updated = '1700-01-01'
LAST_UPDATE_FILE = 'last_update'


class FitbitDatabaseUpdateManager:

    def __init__(self, db_path, db_sections):
        self.last_update_file = configparser.ConfigParser()
        self.database_path = db_path
        self.last_update_file_name = self.database_path + '\\' + LAST_UPDATE_FILE
        self.sections = db_sections

    def handle_db_update_status_file(self):
        if not os.path.exists(self.last_update_file_name) or os.path.getsize(self.last_update_file_name) == 0:
            self.init_database_update_file()
        self.last_update_file.read(self.last_update_file_name)

    def init_database_update_file(self):
        init_db_update_str = ""

        for section_config in self.sections.values():
            init_db_update_str = init_db_update_str + \
                                 '[' + section_config.update_file_param_name + ']\n' \
                                                                               'last_update = ' + never_updated + '\n'

        with open(self.last_update_file_name, 'w') as configfile:
            configfile.write(init_db_update_str)

    def get_last_update_date(self, section):
        return self.last_update_file[section][LAST_UPDATE_PARAM]

    def set_last_update(self, date, section):
        # self.last_update_file['heartrate']['last_update'] = date
        self.last_update_file.set(section, LAST_UPDATE_PARAM, date)
        with open(self.last_update_file_name, 'w') as configfile:
            self.last_update_file.write(configfile)
