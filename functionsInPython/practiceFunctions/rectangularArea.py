"""
Compute the area of a rectangle, given its width and height.
"""

###################################################
# Rectangle area formula

def rectangle_area(width, height):
    """
    Compute the area of a rectangle.
    """
    return width * height




###################################################
# Tests


width, height = 4, 7
print("A rectangle " + str(width) + " inches wide and " + str(height) + 
      " inches high has an area of " + str(rectangle_area(width, height)) + " square inches.")
    
width, height = 7, 4
print("A rectangle " + str(width) + " inches wide and " + str(height) + 
      " inches high has an area of " + str(rectangle_area(width, height)) + " square inches.")

width, height = 10, 10
print("A rectangle " + str(width) + " inches wide and " + str(height) + 
      " inches high has an area of " + str(rectangle_area(width, height)) + " square inches.")

    

