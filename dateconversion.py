import datetime

raw_date = "2017-01-11"
date_format = "%Y-%m-%d"

parsed_date = datetime.datetime.strptime(raw_date, date_format)
date_str = parsed_date.strftime("%m/%d/%y") # 01/11/17
print(date_str)




birthday = "26-January-19"
date_format = "%d-%B-%y"

parsed_date = datetime.datetime.strptime(birthday, date_format)
date_str = parsed_date.strftime("%-m/%-d/%Y")
print(date_str)