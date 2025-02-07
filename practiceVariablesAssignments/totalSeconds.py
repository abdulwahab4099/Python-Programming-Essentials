"""
Solution - Compute the number of seconds in a given number of hours, minutes, and seconds.
"""
hours = 13
minutes = 43
seconds = 9

# Calculate the total seconds in hours
total_seconds = hours * 3600

# Calculate the total seconds in minutes
total_seconds += minutes * 60

# Add the remaining seconds
total_seconds += seconds

print(f"The total number of seconds in {hours} hours, {minutes} minutes, and {seconds} seconds is {total_seconds} seconds.")