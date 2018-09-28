from src.api_calls.FitbitApiCall import FitbitApiCall, api_prefix


class FitbitApiCallHeartRate(FitbitApiCall):

    # /1/user/-/activities/heart/date/{base-date}/{end-date}.json

    # def get_heart_data(self, start_date, end_date):
    #     api_url = api_prefix + 'activities/heart/date/%s/%s/1sec.json' % (start_date, end_date)
    #     response = self.send_api_call(api_url)
    #     return self.handle_response(response)

    def get_data(self, date, start_time, end_time):
        api_url = api_prefix + 'activities/heart/date/%s/1d/1sec/time/%s/%s.json' % (date, start_time, end_time)
        response = self.send_api_call(api_url)
        return self.handle_response(response)

    def get_data_from_json(self, json_obj):
        return json_obj['activities-heart-intraday']['dataset']

    def get_date_from_json(self, json_obj):
        return json_obj['activities-heart'][0]['dateTime']

    def get_columns(self):
        return ['heart_rate']

    def get_time_key_name(self):
        return 'time'

    def get_values_names(self):
        return ['value']

    def get_series_date_format(self):
        return "%Y-%m-%d%H:%M:%S"
