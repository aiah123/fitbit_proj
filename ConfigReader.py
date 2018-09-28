import configparser

class ConfigReader:
    CONFIG_FILE = 'config_file.txt'
    config = None

    def __init__(self, file_name=CONFIG_FILE):
        self.file_name = file_name
        self.read_config()

    def read_config(self):
        self.config = configparser.ConfigParser()
        print(self.file_name)
        self.config.read(self.file_name)

    def get_db_path(self):
        return self.config['prog_params']['database_path']

    def get_first_date(self):
        return self.config['prog_params']['first_day_ever']

    def get_access_token(self):
        return self.config['user_params']['access_token']


