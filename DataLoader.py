from datetime import datetime, date

import pandas as pd
import numpy as np


class DataLoader:

    def __init__(self, database):
        self.db = database

    # return dataframe with the heart rate info from start date to end date
    def get_heart_rate_data(self, start_date, end_date):
        return self.db.get_heart_rate_data(start_date, end_date)

    def get_sleep_data(self, start_date, end_date):
        df = self.db.get_sleep_data(start_date, end_date)
        df['date_no_time'] = df.index
        df['date_no_time'] = df['date_no_time'].apply(lambda x: x.date())

        return df
