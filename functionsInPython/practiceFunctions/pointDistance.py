"""
 Compute the distance between the points (x0, y0) and (x1, y1).
"""

###################################################
# Distance formula

def point_distance(x0, y0, x1, y1):
    """
    Compute the distance between the points (x0, y0) and (x1, y1).
    """
    # Calculate the square of the difference between x-coordinates
    dx = (x1 - x0) ** 2

    # Calculate the square of the difference between y-coordinates
    dy = (y1 - y0) ** 2

    # Return the square root of the sum of the squares  
    return (dx + dy) ** 0.5  # The ** operator is used for exponentiation. The square root is taken using the 0.5 power.  # noqa: E501





###################################################
# Tests



x_0, y_0, x_1, y_1 = 2, 2, 5, 6
print("The distance from (" + str(x_0) + ", " + str(y_0) + ") to (" + 
      str(x_1) + ", " + str(y_1) + ") is " + str(point_distance(x_0, y_0, x_1, y_1)) + ".")

x_0, y_0, x_1, y_1 = 1, 1, 2, 2
print("The distance from (" + str(x_0) + ", " + str(y_0) + ") to (" + 
      str(x_1) + ", " + str(y_1) + ") is " + str(point_distance(x_0, y_0, x_1, y_1)) + ".")

x_0, y_0, x_1, y_1 = 0, 0, 3, 4
print("The distance from (" + str(x_0) + ", " + str(y_0) + ") to (" + 
      str(x_1) + ", " + str(y_1) + ") is " + str(point_distance(x_0, y_0, x_1, y_1)) + ".")


