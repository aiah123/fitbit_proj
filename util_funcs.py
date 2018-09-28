import datetime
date_format = '%Y-%m-%d'

def get_date_from_string(first_data_date):
    return datetime.datetime.strptime(first_data_date, date_format).date()

def log(log_str, log_file_name):
        log_str = str(datetime.datetime.now()) + ' ' + str(log_str)
        with open(log_file_name, "a") as f:
            print(log_str)
            line = str(log_str) + "\n"
            f.write(line)


def create_db_file_name(database_path, current_date, file_prefix, folder, file_type='.json'):
    return database_path + '\\' + folder + '\\' + file_prefix + \
           str(current_date) + file_type
