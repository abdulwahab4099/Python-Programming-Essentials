"""
Compute the area of a triangle (using Heron's formula),
    given its side lengths.
"""

###################################################
# Triangle area (Heron's) formula


def triangle_area(x0, y0, x1, y1, x2, y2):
    """
    Compute the area of a triangle (using Heron's formula),
       given its side lengths.
    """
    # Calculate the lengths of the sides of the triangle
    side1 = ((x1 - x0) ** 2 + (y1 - y0) ** 2) ** 0.5
    side2 = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    side3 = ((x2 - x0) ** 2 + (y2 - y0) ** 2) ** 0.5
    
    # Calculate the semi-perimeter of the triangle
    s = (side1 + side2 + side3) / 2
    
    # Calculate the area using Heron's formula
    area = (s * (s - side1) * (s - side2) * (s - side3)) ** 0.5
    
    return area




###################################################
# Tests


def test(x_0, y_0, x_1, y_1, x_2, y_2):
    """Tests the triangle_area function."""
    
    print("A triangle with vertices (" + str(x_0) + "," + str(y_0) + "),")
    print("(" + str(x_1) + "," + str(y_1) + "), and")
    print("(" + str(x_2) + "," + str(y_2) + ") has an area of")
    print(str(triangle_area(x_0, y_0, x_1, y_1, x_2, y_2)) + ".")

x_0, y_0, x_1, y_1, x_2, y_2 = 0, 0, 3, 4, 1, 1
print("A triangle with vertices (" + str(x_0) + ", " + str(y_0) + "), (" + 
      str(x_1) + "," + str(y_1) + "), and (" + str(x_2) + ", " + str(y_2) + 
      ") has an area of " + str(triangle_area(x_0, y_0, x_1, y_1, x_2, y_2)) + ".")

x_0, y_0, x_1, y_1, x_2, y_2 = -2, 4, 1, 6, 2, 1
print("A triangle with vertices (" + str(x_0) + ", " + str(y_0) + "), (" + 
      str(x_1) + "," + str(y_1) + "), and (" + str(x_2) + ", " + str(y_2) + 
      ") has an area of " + str(triangle_area(x_0, y_0, x_1, y_1, x_2, y_2)) + ".")

x_0, y_0, x_1, y_1, x_2, y_2 = 10, 0, 0, 0, 0, 10
print("A triangle with vertices (" + str(x_0) + ", " + str(y_0) + "), (" + 
      str(x_1) + "," + str(y_1) + "), and (" + str(x_2) + ", " + str(y_2) + 
      ") has an area of " + str(triangle_area(x_0, y_0, x_1, y_1, x_2, y_2)) + ".")


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#A triangle with vertices (0,0), (3,4), and (1,1) has an area of 0.5.
#A triangle with vertices (-2,4), (1,6), and (2,1) has an area of 8.5.
#A triangle with vertices (10,0), (0,0), and (0,10) has an area of 50.
