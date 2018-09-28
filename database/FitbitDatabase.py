from src.database.FitbitDatabaseReader import *
from src.database.FitbitDatabaseWriter import *
from src.util_funcs import get_date_from_string
from src.database.FitbitDatabaseSectionsConfig import FitbitDatabaseSectionsConfig

LOG_FILE_NAME = 'database.log'
DB_CONFIG_FILE = 'database_conf'


class FitbitDatabase:

    def __init__(self, config):
        self.db_sections_config = FitbitDatabaseSectionsConfig(config)
        self.database_path = config.get_db_path()
        self.sections = self.db_sections_config.sections_dict
        self.log_file_name = self.database_path + '/' + LOG_FILE_NAME
        self.__create_db_struct()
        self.first_data_date = get_date_from_string(config.get_first_date())
        self.db_reader = FitbitDatabaseReader(self.database_path, self.sections)
        self.db_writer = FitbitDatabaseWriter \
            (self.sections, self.database_path, self.first_data_date, self.log_file_name)

    def get_heart_rate_data(self, start_date, end_date):
        return self.db_reader.get_heart_rate_data(start_date, end_date)

    def get_sleep_data(self, start_date, end_date):
        return self.db_reader.get_sleep_data(start_date, end_date)


    def update_heart_rate(self):
        section_config = self.sections[self.db_sections_config.HEART_RATE_SECTION_CONFIG]
        return self.db_writer.update_section(section_config)

    def update_sleep(self):
        section_config = self.sections[self.db_sections_config.SLEEP_SECTION_CONFIG]
        return self.db_writer.update_section(section_config)

    def __create_db_struct(self):
        for section_config in self.sections.values():
            db_folder = self.database_path + '\\' + section_config.db_folder
            if not os.path.exists(db_folder):
                os.makedirs(db_folder)
