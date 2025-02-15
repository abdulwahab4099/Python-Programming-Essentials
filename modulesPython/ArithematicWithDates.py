import datetime

date1 = datetime.date(2006, 3, 15)
date2 = datetime.date(2009, 4, 30)
difference = date2 - date1

print(difference)
print(difference.days)

date3 = date1 + difference
print(date2 == date3)

print(datetime.date.today())

print(datetime.date.today().strftime("%B %d, %Y"))

print(datetime.date.today().strftime("%A, %B %d, %Y"))

print(datetime.date.today().strftime("%Y-%m-%d"))

print(datetime.date.today().strftime("%Y/%m/%d"))

print(datetime.date.today().strftime("%d-%m-%Y"))

print(datetime.date.today().strftime("%d/%m/%Y"))

print(datetime.date.today().strftime("%Y-%m-%d %H:%M:%S"))

print(datetime.date.today().strftime("%Y/%m/%d %H:%M:%S"))

print(datetime.date.today().strftime("%d-%m-%Y %H:%M:%S"))

print(datetime.date.today().strftime("%d/%m/%Y %H:%M:%S"))

print(datetime.date.today().strftime("%Y-%m-%d %H:%M:%S %p"))

print(datetime.date.today().strftime("%Y/%m/%d %H:%M:%S %p"))

print(datetime.date.today().strftime("%d-%m-%Y %H:%M:%S %p"))

print(datetime.date.today().strftime("%d/%m/%Y %H:%M:%S %p"))

print(datetime.date.today().strftime("%A, %B %d, %Y %H:%M:%S %p"))

print(datetime.date.today().strftime("%A, %B %d, %Y %I:%M:%S %p"))

print(datetime.date.today().strftime("%A, %B %d, %Y %I:%M:%S %p %Z"))

print(datetime.date.today().strftime("%A, %B %d, %Y %I:%M:%S %p %z"))

print(datetime.date.today().strftime("%A, %B %d, %Y %I:%M:%S %p %Z %Y"))

print(datetime.date.today().strftime("%A, %B %d, %Y %I:%M:%S %p %z %Y-%m"))

print(datetime.date.today().strftime("%A, %B %d, %Y %I:%M:%S %p %z %Y-%m-%d"))

print(datetime.date.today().strftime("%A, %B %d, %Y %I:%M:%S %p %z %Y-%m-%d %H"))

print(datetime.date.today().strftime("%A, %B %d, %Y %I:%M:%S %p %z %Y-%m-%d %H:%M"))

print(datetime.date.today().strftime("%A, %B %d, %Y %I:%M:%S %p %z %Y-%m-%d %H:%M:%S"))

print(datetime.date.today().strftime("%A, %B %d, %Y %I:%M:%S %p %z %Y-%m-%d %H:%M:%S.%f"))

print(datetime.date.today().strftime("%A, %B %d, %Y %I:%M:%S %p %z %Y-%m-%d %H:%M:%S.%f %Z"))

print(datetime.date.today().strftime("%A, %B %d, %Y %I:%M:%S %p %z %Y-%m-%d %H:%M:%S.%f %Z %Y-%m-%d"))

print(datetime.date.today().strftime("%A, %B %d, %Y %I:%M:%S %p %z %Y-%m-%d %H:%M:%S.%f %Z %Y-%m"))

print(datetime.date.today().strftime("%A, %B %d, %Y %I:%M:%S %p %z %Y-%m-%d %H:%M:%S.%f %Z %Y-%m-%d"))

print(datetime.date.today().strftime("%A, %B %d, %Y %I:%M:%S %p %z %Y-%m-%d %H:%M:%S.%f %Z %Y-%m-%d %H"))

print(datetime.date.today().strftime("%A, %B %d, %Y %I:%M:%S %p %z %Y-%m-%d %H:%M:%S.%f %Z %Y-%m-%d %H:%M"))

print(datetime.date.today().strftime("%A, %B %d, %Y %I:%M:%S %p %z %Y-%m-%d %H:%M:%S.%f %Z %Y-%m-%d %H:%M:%S"))

print(datetime.date.today().strftime("%A, %B %d, %Y %I:%M:%S %p %z %Y-%m-%d %H:%M:%S.%f %Z %Y-%m-%d %H:%M:%S.%f %Y-%m-%d"))

print(datetime.date.today().strftime("%A, %B %d, %Y %I:%M:%S %p %z %Y-%m-%d %H:%M:%S.%f %Z %Y-%m-%d %H:%M:%S.%f %Y-%m"))

print(datetime.date.today().strftime("%A, %B %d, %Y %I:%M:%S %p %z %Y-%m-%d %H:%M:%S.%f %Z %Y-%m-%d %H:%M:%S.%f %Y-%m-%d"))

print(datetime.date.today().strftime("%A, %B %d, %Y %I:%M:%S %p %z %Y-%m-%d %H:%M:%S.%f %Z %Y-%m-%d %H:%M:%S.%f %Y-%m-%d %H"))

print(datetime.date.today().strftime("%A, %B %d, %Y %I:%M:%S %p %z %Y-%m-%d %H:%M:%S.%f %Z %Y-%m-%d %H:%M:%S.%f %Y-%m-%d"))

print(datetime.date.today().strftime("%A, %B %d, %Y %I:%M:%S %p %z %Y-%m-%d %H:%M:%S.%f %Z %Y-%m-%d %H:%M:%S.%f %Y-%m-%d %H:%M"))

print(datetime.date.today().strftime("%A, %B %d, %Y %I:%M:%S %p %z %Y-%m-%d %H:%M:%S.%f %Z %Y-%m-%d %H:%M:%S.%f %Y-%m-%d %H:%M:%S.%f"))

print(datetime.date.today().strftime("%A, %B %d, %Y %I:%M:%S %p %z %Y-%m-%d %H:%M:%S.%f %Z %Y-%m-%d %H:%M:%S.%f %Y-%m-%d %H:%M:%S.%f %Y-%m"))

print(datetime.date.today().strftime("%A, %B %d, %Y %I:%M:%S %p %z %Y-%m-%d %H:%M:%S.%f %Z %Y-%m-%d %H:%M:%S.%f %Y-%m-%d %H:%M:%S.%f"))

print(datetime.date.today().strftime("%A, %B %d, %Y %I:%M:%S %p %z %Y-%m-%d %H:%M:%S.%f %Z %Y-%m-%d %H:%M:%S.%f %Y-%m-%d %H:%M:%S.%f %Y-%m-%d %H:%M:%S.%f"))

print(datetime.date.today().strftime("%A, %B %d, %Y %I:%M:%S %p %z %Y-%m-%d %H:%M:%S.%f %Z %Y-%m-%d %H:%M:%S.%f %Y-%m-%d %H:%M:%S.%f %Y-%m-%d %H:%M:%S.%f %Y-%m-%d"))

