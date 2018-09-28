import datetime
import pandas as pd

from src.database.FitbitDatabaseSectionsConfig import FitbitDatabaseSectionsConfig
from src.util_funcs import create_db_file_name


class FitbitDatabaseReader:

    def __init__(self, db_path, db_sections):
        self.sections = db_sections
        self.db_path = db_path

    # returns the list of jsons (each element is a data from a day) for the requested dates
    def get_heart_rate_data(self, start_date, end_date):
        section_config = self.sections[FitbitDatabaseSectionsConfig.HEART_RATE_SECTION_CONFIG]
        return self.get_pickled_data(end_date, section_config, start_date)

    def get_sleep_data(self, start_date, end_date):
        section_config = self.sections[FitbitDatabaseSectionsConfig.SLEEP_SECTION_CONFIG]
        return self.get_pickled_data(end_date, section_config, start_date)

    def get_pickled_data(self, end_date, section_config, start_date):
        curr_date = start_date
        day_delta = datetime.timedelta(days=1)
        df_list = []
        while curr_date <= end_date:
            file_name = create_db_file_name(self.db_path, curr_date, section_config.db_file_prefix,
                                            section_config.db_folder, '.pkl')
            df_list.append(pd.read_pickle(file_name))
            curr_date = curr_date + day_delta
        return pd.concat(df_list)
