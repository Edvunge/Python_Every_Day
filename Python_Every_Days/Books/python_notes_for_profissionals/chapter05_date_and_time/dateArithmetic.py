import datetime

today = datetime.date.today()
print('Today:', today)

yesterday = today - datetime.timedelta(days=1)
print('yesterday: ', yesterday)

tomorrow = today + datetime.timedelta(days=1)
print('Tomorrow: ', tomorrow)

print('Time between tomorrow and yesterday:', tomorrow - yesterday)