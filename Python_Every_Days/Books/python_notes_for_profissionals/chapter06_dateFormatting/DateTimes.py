from datetime import datetime

a = datetime(2016, 10, 6, 0, 0, 0)
b = datetime(2016, 10, 1, 23, 59, 59)

a-b

(a-b).days

(a-b).total_seconds()