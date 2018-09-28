import datetime

import pandas as pd


class DataAnalyzer:

    def __init__(self, data_loader):
        self.dl = data_loader


    def get_sleep_scores(self, start_date, end_date):
        sleep_data = self.dl.get_sleep_data(start_date, end_date)

        date_column = 'date'
        score_column = 'score'
        df = pd.DataFrame(columns=[date_column, score_column])

        curr = start_date
        scores = []
        dates = []

        while curr <= end_date:
            curr = curr +  datetime.timedelta(days=1)
            scores.append(self.__get_single_day_sleep_score(curr, sleep_data))
            dates.append(curr)

        df[date_column] = dates
        df[score_column] = scores
        df.set_index([date_column], drop=True, inplace=True)

        return df

    def __get_single_day_sleep_score(self, day, sleep_data):
        return sum(sleep_data[(sleep_data['date_no_time'] == day) & (sleep_data['level'] == 'deep')]['seconds'])

