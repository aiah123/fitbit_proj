import requests
import abc

api_version = '1.2'
api_prefix = 'https://api.fitbit.com/%s/user/-/' % api_version


class FitbitApiCall:
    def __init__(self, access_token):
        self.access_token = access_token

    def send_api_call(self, url):
        header = {'Authorization': 'Bearer ' + self.access_token}
        response = requests.get(url, headers=header)
        return response

    @staticmethod
    def handle_response(response):
        if response.status_code != 200:
            print('Error! status code: %d. Content:\n %s' % (response.status_code, response.content))
            return 0, 0
        else:
            return response

    @abc.abstractmethod
    def get_data(self, date, start_time, end_time):
        """get the data from fitbit cloud"""
        return

    @abc.abstractmethod
    def get_data_from_json(self, json_obj):
        "get the data from the json response"
        return

    @abc.abstractmethod
    def get_date_from_json(self, json_obj):
        "get the data from the json response"
        return

    @abc.abstractmethod
    def get_columns(self):
        "get the data from the json response"
        return

    @abc.abstractmethod
    def get_time_key_name(self):
        "get the name of the json key of the time value in the time series"
        return

    @abc.abstractmethod
    def get_values_names(self):
        "get the name of the json keys that are the values in the time series (i.e, not date)"
        return

    @abc.abstractmethod
    def get_series_date_format(self):
        "get the time format as appears in the json time series"
        return