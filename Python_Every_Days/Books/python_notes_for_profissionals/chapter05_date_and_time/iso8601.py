import iso8601

iso8601.parse_date('2016-07-22 09:25:59')

iso8601.parse_date('2016-07-22 09:25:59+03:00')

iso8601.parse_date('2016-07-22 09:25:59z')

iso8601.parse_date('2016-07-22 09:25:59.000111+03:00')

iso8601.parse_date('2016-07-22 09:25:59', default_timezone=None)

iso8601.parse_date('2016-07-22 09:25:59z', default_timezone=None)
