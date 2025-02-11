"""
Compute the area of a circle, given the length of its radius.
"""

# Import the math module to access the exact value of pi
import math
PI = math.pi

###################################################
# Circle area formula

def circle_area(radius):
    """
    Given the length of the radius, compute and return the area of a circle.
    """
    return PI * radius**2





###################################################
# Tests


radius = 8
print("A circle with a radius of " + str(radius) + 
      " inches has an area of " + str(circle_area(radius)) + 
      " square inches.")

radius = 3
print("A circle with a radius of " + str(radius) + 
      " inches has an area of " + str(circle_area(radius)) + 
      " square inches.")

radius = 12.9
print("A circle with a radius of " + str(radius) + 
      " inches has an area of " + str(circle_area(radius)) + 
      " square inches.")


