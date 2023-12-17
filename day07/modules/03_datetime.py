import datetime


my_time = datetime.time(13, 20, 2, 20)

print(my_time)

print(my_time.minute)

print(my_time.hour)

today = datetime.date.today()
print(today)
print(f'Year: {today.year}. Month: {today.month}')
print(today.ctime())

my_datetime = datetime.datetime(2023, 12, 17,14, 20, 1)
print(my_datetime)

my_datetime = my_datetime.replace(year=2022)
print(my_datetime)

date1 = datetime.date(2023, 12, 17)
date2 = datetime.date(2023, 5, 3)

result = date1 - date2

# Works for datetime objects as well
print(result)
print(type(result))
