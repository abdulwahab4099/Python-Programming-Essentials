import datetime

todays_date = datetime.date.today()

print(todays_date)

# Get the day of the week for the current date
day_of_week = todays_date.strftime("%A")

print(f"Today is {day_of_week}.")

# Get the number of days left until the end of the month

last_day_of_month = todays_date.replace(day=1) + datetime.timedelta(days=31)

days_left_in_month = (last_day_of_month - todays_date).days

print(f"There are {days_left_in_month} days left in the month.")

# Get the number of weeks left until the end of the month
weeks_left_in_month = days_left_in_month // 7

print(f"There are {weeks_left_in_month} weeks left in the month.")

# Get the number of months left until the end of the year
months_left_in_year = (datetime.date(todays_date.year, 12, 31)
                        - todays_date).days // 30

print(f"There are {months_left_in_year} months left in the year.")

# Get the number of years left until the end of the century
years_left_in_century = (datetime.date(todays_date.year + 99, 12
                                       , 31) - todays_date).days // 365

print(f"There are {years_left_in_century} years left in the century.")

# Get the number of leap years left until the end of the century
leap_years_left_in_century = years_left_in_century // 4

print(f"There are {leap_years_left_in_century} leap years left in the century.")    

# Get the number of days in the current year

days_in_year = (datetime.date(todays_date.year + 1, 1, 1)
                        - datetime.date(todays_date.year, 1, 1)).days

print(f"There are {days_in_year} days in the current year.")

# Get the number of weeks in the current year
weeks_in_year = days_in_year // 7

print(f"There are {weeks_in_year} weeks in the current year.")

# Get the number of months in the current year
months_in_year = 12

print(f"There are {months_in_year} months in the current year.")

# Get the number of years in the current century

years_in_century = 100

print(f"There are {years_in_century} years in the current century.")

# Get the number of leap years in the current century

leap_years_in_century = years_in_century // 4

print(f"There are {leap_years_in_century} leap years in the current century.")

# Get the number of days in the next year
todays_date = datetime.date.today()

next_year = todays_date.year + 1

days_in_next_year = (datetime.date(next_year, 1, 1)
                        - datetime.date(next_year - 1, 1, 1)).days

print(f"There are {days_in_next_year} days in the next year.")

# Get the number of weeks in the next year
weeks_in_next_year = days_in_next_year // 7

print(f"There are {weeks_in_next_year} weeks in the next year.")

# Get the number of months in the next year


months_in_next_year = 12

print(f"There are {months_in_next_year} months in the next year.")

# Get the number of years in the next century
years_in_next_century = 100

print(f"There are {years_in_next_century} years in the next century.")
