from datetime import datetime

from Books.python_notes_for_profissionals.chapter06_dateFormatting.outPuttingDateTime import datetime_string_format

datetime_string = 'Oct 1 2016, 00:00:00'
datetime_string_format = '%b %d %Y, %H:%M:%S'
datetime.strptime(datetime_string, datetime_string_format)
