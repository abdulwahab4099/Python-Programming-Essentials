"""
Solution - Compute the future value of a given present value, annual rate, and number of years.
"""

present_value = 1000
annual_rate = 9.5
years = 7

future_value = present_value * (1 + 0.01 * annual_rate) ** years


print("The future value of $" + str(present_value) + " in " + str(years) + 
      " years at an annual rate of " + str(annual_rate) + "% is $" + str(future_value) + ".")
