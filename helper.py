import datetime


def get_time(you_timestamp):
    datetime_result = datetime.datetime.fromtimestamp(int(you_timestamp) / 1e3)
    return datetime_result
