"""
Compute and print tens and ones digit of an integer in [0,100).
"""

###################################################
# Digits function

def print_digits(n):
    """Prints the tens and ones digits of n."""
    # Get the last two digits of n
    tens_digit = n // 10
    ones_digit = n % 10
    
    # Print the digits
    print("The tens digit is", tens_digit, ", and the ones digit is", ones_digit, ".")  
    
    return tens_digit, ones_digit




    
###################################################
# Tests

    
print_digits(42)
print_digits(99)
print_digits(5)


