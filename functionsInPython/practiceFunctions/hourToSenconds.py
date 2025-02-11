"""
Compute the number of seconds in a given number of hours, minutes, and seconds.
"""

###################################################
# hours_to_minutes function
def hours_to_minutes(hours, minutes, seconds):
    return hours * 60 * 60 + minutes * 60 + seconds

def total_seconds(hours, minutes, seconds):
    return hours_to_minutes(hours, minutes, seconds)





###################################################
# Tests


hours, minutes, seconds = 7, 21, 37
print(str(hours) + " hours, " + str(minutes) + " minutes, and " + 
      str(seconds) + " seconds totals to " + str(total_seconds(hours, minutes, seconds)) + 
      " seconds.")

hours, minutes, seconds = 10, 1, 7
print(str(hours) + " hours, " + str(minutes) + " minutes, and " + 
      str(seconds) + " seconds totals to " + str(total_seconds(hours, minutes, seconds)) + 
      " seconds.")

hours, minutes, seconds = 1, 0, 1
print(str(hours) + " hours, " + str(minutes) + " minutes, and " + 
      str(seconds) + " seconds totals to " + str(total_seconds(hours, minutes, seconds)) + 
      " seconds.")

