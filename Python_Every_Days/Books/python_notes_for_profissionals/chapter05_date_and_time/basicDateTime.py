import datetime

today = datetime.date.today()
new_year = datetime.date(2017, 1, 1)

noon = datetime.time(12, 0, 0)

now = datetime.datetime.now()

millenium_turn = datetime.datetime(2000, 1, 1, 0, 0, 0)
print(millenium_turn)

print('Time since the millenium at midnight: ', datetime.datetime(today.year, today.month, today.day) - millenium_turn)
print('Time since the millenium at noon: ', datetime.datetime.combine(today, noon) - millenium_turn)
