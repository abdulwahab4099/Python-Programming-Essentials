"""
Compute the future value of a given present value, annual rate, and number of years.
"""

###################################################
# Future value formula


def future_value(present_value, annual_rate, years):
    # Calculate the future value using the formula: future_value = present_value * (1 + annual_rate/100)^years
    return present_value * (1 + annual_rate/100)**years





###################################################
# Tests



present_value, annual_rate, years = 1000, 7, 10	
print("The future value of $" + str(present_value) + " in " + str(years) + 
      " years at an annual rate of " + str(annual_rate) + "% is $" + 
      str(future_value(present_value, annual_rate, years)) + ".")
    
present_value, annual_rate, years = 200, 4, 5
print("The future value of $" + str(present_value) + " in " + str(years) + 
      " years at an annual rate of " + str(annual_rate) + "% is $" + 
      str(future_value(present_value, annual_rate, years)) + ".")

present_value, annual_rate, years = 1000, 3, 20
print("The future value of $" + str(present_value) + " in " + str(years) + 
      " years at an annual rate of " + str(annual_rate) + "% is $" + 
      str(future_value(present_value, annual_rate, years)) + ".")



