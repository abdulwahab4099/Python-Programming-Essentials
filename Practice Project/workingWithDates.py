"""
Project for Week 4 of "Python Programming Essentials".
Collection of functions to process dates.

@Author: Abdul Wahab 
"""
import datetime

def is_leap_year(year):
    
    """
    Returns True if the given year is a leap year, otherwise False.
    """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def days_in_month(year, month):
    """
    Returns the number of days in the given month of the given year.
    """
    month_days = {1: 31, 2: (29 if is_leap_year(year) else 28), 3: 31, 4: 30, 5: 31, 6: 30,
                  7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    
    return month_days.get(month, 0)

def is_valid_date(year, month, day):
    """
    Returns True if the given year-month-day is a valid date, otherwise False.
    """
    if not (1 <= year <= 9999):  # **Fixed the upper limit check**
        return False
    if not (1 <= month <= 12):
        return False
    return 1 <= day <= days_in_month(year, month) 

def days_since_start(year, month, day):
    """
    Returns the total number of days from year 1, month 1, day 1 to the given date.
    """
    if not is_valid_date(year, month, day):
        return 0
    
    days = sum(366 if is_leap_year(y) else 365 for y in range(1, year))
    days += sum(days_in_month(year, m) for m in range(1, month))
    days += day
    return days

def days_between(year1, month1, day1, year2, month2, day2):
    """
    Returns the number of days from the first date to the second date.
    0 is returned if either of the dates is invalid.
    """
    
    if not (is_valid_date(year1, month1, day1) and is_valid_date(year2, month2, day2)):
        return 0
    
    return max(0, days_since_start(year2, month2, day2) - days_since_start(year1, month1, day1))

def age_in_days(year, month, day):
    """
    Returns the age in days from the given birthday to today.
    0 is returned if the date is invalid.
    """     
    TODAY_YEAR, TODAY_MONTH, TODAY_DAY = 2025, 2, 20  # Use actual current date
    
    return days_between(year, month, day, TODAY_YEAR, TODAY_MONTH, TODAY_DAY)


print(days_in_month(2024, 2))  # Should print 29 (Leap Year)
print(is_valid_date(2025, 2, 29))  # Should return False (2025 is not a leap year)
print(days_between(2024, 2, 20, 2025, 2, 20))  # Should return 366
print(age_in_days(2000, 1, 1))  # Should return the age in days

print(days_since_start(2025, 2, 20))  # Should return the number of days since 1/1/2025

# Test the function with a date in the future
print(days_between(2025, 2, 20, 2026, 2, 20))

# Test the function with a date in the past

print(days_between(2025, 2, 20, 2024, 2, 20))

# Test the function with an invalid date

print(days_between(2025, 2, 30, 2025, 2, 20))  # Should return 0 (Invalid date) 

# Test the function with an invalid date

print(days_between(2025, 13, 20, 2025, 2, 20))  # Should return 0 (Invalid month)

# Test the function with an invalid date

print(days_between(1900, 2, 20, 2025, 2, 20))  # Should return 0 (Invalid year)

# Test the function with an invalid date

print(days_between(2025, 2, 20, 1899, 2, 20))  # Should return 0 (Invalid year)

# Test the function with an invalid date

print(days_between(2025, 2, 20, 2025, 2, 31))  # Should return 0 (Invalid day)

# Test the function with an invalid date

print(days_between(2025, 2, 20, 2025, 1, 1))  # Should return 0 (Invalid day)