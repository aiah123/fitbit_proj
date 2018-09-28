from src.api_calls.FitbitApiCall import FitbitApiCall, api_prefix


class FitbitApiCallSleep(FitbitApiCall):

    # def get_heart_data(self, date='2018-07-23', num_of_days='1'):
    #     api_url = api_prefix + 'activities/heart/date/%s/%sd/1sec.json' % (api_prefix, date, num_of_days)
    #     response = self.send_api_call(api_url)
    #     return self.handle_response(response)

    def get_data(self, date, start_time, end_time):
        api_url = api_prefix + 'sleep/date/%s.json' % (date)
        response = self.send_api_call(api_url)
        return self.handle_response(response)

    def get_data_from_json(self, json_obj):
        if len(json_obj['sleep']) > 0:
            return json_obj['sleep'][0]['levels']['data']
        else:
            return []

    def get_date_from_json(self, json_obj):
        return '' #json_obj['sleep'][0]['dateOfSleep']

    def get_columns(self):
        return ['level', 'seconds']

    def get_time_key_name(self):
        return 'dateTime'

    def get_values_names(self):
        return ['level', 'seconds']

    # "2018-07-27T08:00:30.000"
    def get_series_date_format(self):
        return "%Y-%m-%dT%H:%M:%S.%f"