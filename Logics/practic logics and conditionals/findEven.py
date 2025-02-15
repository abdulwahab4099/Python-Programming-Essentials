"""
Compute whether an integer is even.
"""

###################################################
# Is even formula

def is_even(x):
    return x % 2 == 0





###################################################
# Tests


number = 8
if is_even(number):
    print(number, "is even.")
else:
    print(number, "is odd.")
    
number = 3
if is_even(number):
    print(number, "is even.")
else:
    print(number, "is odd.")
    
number = 12
if is_even(number):
    print(number, "is even.")
else:
    print(number, "is odd.")

