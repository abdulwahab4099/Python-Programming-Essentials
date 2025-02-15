import datetime

date1 = datetime.date(2006, 3, 15)
date2 = datetime.date(2009, 4, 30)

print(date1 != date2)
print(date1 > date2)
print(date1 < date2)

date3 = date1.replace(year=2010)

print(date1 == date3)

delta = date2 - date1

print(delta.days)

date4 = date1 + datetime.timedelta(days=365)

print(date4)

date5 = date1 + datetime.timedelta(weeks=2)

print(date5)
