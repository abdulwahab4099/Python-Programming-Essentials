"""
Compute whether two intervals intersect.
"""

###################################################
# Interval intersection formula

def interval_intersect(lower1, upper1, lower2, upper2):
    """
    Compute whether two intervals intersect.
    """
    return lower1 <= upper2 and lower2 <= upper1





###################################################
# Tests


int1_lower, int1_upper, int2_lower, int2_upper = 0, 1, 1, 2
print("Intervals [" + str(int1_lower) + ", " + str(int1_upper) + "] and [" + 
      str(int2_lower) + ", " + str(int2_upper) + "] ", end = "")
if interval_intersect(int1_lower, int1_upper, int2_lower, int2_upper):
    print("intersect.")
else:
    print("do not intersect.")
    
int1_lower, int1_upper, int2_lower, int2_upper = 1, 2, 0, 1
print("Intervals [" + str(int1_lower) + ", " + str(int1_upper) + "] and [" + 
      str(int2_lower) + ", " + str(int2_upper) + "] ", end = "")
if interval_intersect(int1_lower, int1_upper, int2_lower, int2_upper):
    print("intersect.")
else:
    print("do not intersect.")
    
int1_lower, int1_upper, int2_lower, int2_upper = 0, 1, 2, 3
print("Intervals [" + str(int1_lower) + ", " + str(int1_upper) + "] and [" + 
      str(int2_lower) + ", " + str(int2_upper) + "] ", end = "")
if interval_intersect(int1_lower, int1_upper, int2_lower, int2_upper):
    print("intersect.")
else:
    print("do not intersect.")
    
int1_lower, int1_upper, int2_lower, int2_upper = 2, 3, 0, 1
print("Intervals [" + str(int1_lower) + ", " + str(int1_upper) + "] and [" + 
      str(int2_lower) + ", " + str(int2_upper) + "] ", end = "")
if interval_intersect(int1_lower, int1_upper, int2_lower, int2_upper):
    print("intersect.")
else:
    print("do not intersect.")
    
int1_lower, int1_upper, int2_lower, int2_upper = 0, 3, 1, 2
print("Intervals [" + str(int1_lower) + ", " + str(int1_upper) + "] and [" + 
      str(int2_lower) + ", " + str(int2_upper) + "] ", end = "")
if interval_intersect(int1_lower, int1_upper, int2_lower, int2_upper):
    print("intersect.")
else:
    print("do not intersect.")
    

