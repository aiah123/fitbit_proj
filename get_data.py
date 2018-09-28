from src.ConfigReader import ConfigReader
from src.DataLoader import DataLoader
from src.DataAnalyzer import DataAnalyzer
from src.database.FitbitDatabase import *

import matplotlib as pyplot

MATI_START_DATE = "2018-08-12"
MATI_END_DATE = "2018-08-18"
ABBA_START_DATE = "2018-08-05"
ABBA_END_DATE = "2018-08-11"


def main():

    config = ConfigReader()

    db = FitbitDatabase(config)
    # db.update_heart_rate()
    # db.update_sleep()


    dl = DataLoader(db)
    # hr_data = dl.get_heart_rate_data(start_date, end_date)
    # sleep_data = dl.get_sleep_data(start_date, end_date)
    #
    # print(hr_data)
    # print(sleep_data)

    da = DataAnalyzer(dl)

    mati_sleep_score = da.get_sleep_scores(
        get_date_from_string(MATI_START_DATE), get_date_from_string(MATI_END_DATE))

    mati_sleep_score = da.get_sleep_scores(
        get_date_from_string(MATI_START_DATE), get_date_from_string(MATI_END_DATE))

    # get_sleep_score(start_date, end_date)



if __name__ == '__main__':
    main()
