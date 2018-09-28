from collections.__init__ import namedtuple

from src.api_calls.FitbitAuthorization import FitbitAuthorization
from src.api_calls.FitbitApiCallHeartRate import FitbitApiCallHeartRate
from src.api_calls.FitbitApiCallSleep import FitbitApiCallSleep


class FitbitDatabaseSectionsConfig:
    SLEEP_SECTION_CONFIG = 'sleep_section_config'
    HEART_RATE_SECTION_CONFIG = 'heart_rate__section_config'

    SectionConfig = namedtuple('SectionConfig', 'db_folder db_file_prefix update_file_param_name api_call_class')

    def __init__(self, config):
        self.heartRateConfig = self.SectionConfig(db_file_prefix='heartrate_',
                                                  db_folder='heart_rate',
                                                  update_file_param_name='heartrate',
                                                  api_call_class=
                                                  FitbitApiCallHeartRate(FitbitAuthorization(config).get_access_token()))
        self.sleepConfig = self.SectionConfig(db_file_prefix='sleep_',
                                         db_folder='sleep',
                                         update_file_param_name='sleep',
                                         api_call_class=
                                         FitbitApiCallSleep(FitbitAuthorization(config).get_access_token()))

        self.sections_dict = {self.HEART_RATE_SECTION_CONFIG: self.heartRateConfig,
                              self.SLEEP_SECTION_CONFIG: self.sleepConfig}

