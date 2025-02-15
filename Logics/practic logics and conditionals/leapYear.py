"""
Compute whether the given year is a leap year.
"""

###################################################
# Is leapyear formula

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0





###################################################
# Tests


year = 2000
if is_leap_year(year):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
    
year = 1996
if is_leap_year(year):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
    
year = 1800
if is_leap_year(year):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
    
year = 2013
if is_leap_year(year):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
    

