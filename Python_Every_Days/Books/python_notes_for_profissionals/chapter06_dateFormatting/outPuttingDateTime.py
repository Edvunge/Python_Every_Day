from datetime import datetime

datetime_for_string = datetime(2016, 10, 1, 0, 0)
datetime_string_format = '%b %d %Y, %H:%M:%S'
datetime.strptime(datetime_for_string, datetime_string_format)



