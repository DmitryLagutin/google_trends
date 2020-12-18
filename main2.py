import datetime

you_timestamp = 1607698800000

datetime = datetime.datetime.fromtimestamp(you_timestamp / 1e3)
print(type(datetime))
print(datetime)
