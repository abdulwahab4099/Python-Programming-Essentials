"""
Compute and print powerball numbers.
"""

import random

###################################################
# Powerball function


def powerball():
    """
    Prints Powerball lottery numbers.
    """
    
    # Note that including the optional argument end = "" to print() cause
    # print to NOT generate a newline
    
    print("Today's numbers are " + str(random.randrange(1, 60)) + ", ", end = "")
    print(str(random.randrange(1, 60)) + ", ", end = "")
    print(str(random.randrange(1, 60)) + ", ", end = "") 
    print(str(random.randrange(1, 60)) + ", and ", end = "")
    print(str(random.randrange(1, 60)) + ". The Powerball number is ",  end = "") 
    print(str(random.randrange(1, 36)) + ".")

    
###################################################
# Tests

    
powerball()
powerball()
powerball()

###################################################################
# Some sample output appears below.  Note that numbers need not match
#Today's numbers are 46, 25, 49, 54, and  8. The Powerball number is 26.
#Today's numbers are 14, 11, 17, 6, and  30. The Powerball number is 16.
#Today's numbers are 58, 59, 39, 2, and  29. The Powerball number is 19.
