"""
Compute the circumference of a circle, given the length of its radius.
"""

import math
PI = math.pi

###################################################
# Circle circumference formula

def circle_circumference(radius):
    return 2 * PI * radius





###################################################
# Tests


radius = 8
print("A circle with a radius of " + str(radius) + 
      " inches has a circumference of " + str(circle_circumference(radius)) + " inches.")

radius = 3
print("A circle with a radius of " + str(radius) + 
      " inches has a circumference of " + str(circle_circumference(radius)) + " inches.")

radius = 12.9
print("A circle with a radius of " + str(radius) + 
      " inches has a circumference of " + str(circle_circumference(radius)) + " inches.")
