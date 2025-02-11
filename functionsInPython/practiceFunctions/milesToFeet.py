"""
Compute the number of feet corresponding to a number of miles.
"""




###################################################
# Miles to feet conversion formula

def miles_to_feet(miles):
    return 5280 * miles



###################################################
# Tests



miles = 13
print(str(miles) + " miles equals " + str(miles_to_feet(miles)) + " feet.")
    
miles = 57
print(str(miles) + " miles equals " + str(miles_to_feet(miles)) + " feet.")

miles = 82.67
print(str(miles) + " miles equals " + str(miles_to_feet(miles)) + " feet.")


