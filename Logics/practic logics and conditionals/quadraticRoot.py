"""
Solution - Compute the smaller root of a quadratic equation.
"""

###################################################
# Smaller quadratic root formula
# a*x^2 + b*x + c = 0
def smaller_root(coeff_a, coeff_b, coeff_c):
    """
    Returns the smaller root of a quadratic equation with the
    given coefficients.
    """
    
    discriminant = coeff_b ** 2 - 4 * coeff_a * coeff_c
    if discriminant < 0 or coeff_a == 0:
        print("Error: No real solutions")
    else:
        discriminant_sqrt = discriminant ** 0.5
        # Choose the positive or negative square root that leads to a smaller root.
        if coeff_a > 0:
            smaller = - discriminant_sqrt
        else:
            smaller = discriminant_sqrt
        return (-coeff_b + smaller) / (2 * coeff_a)


###################################################
# Tests

coeff_a, coeff_b, coeff_c = 1, -3, 2
print("The smaller root of " + str(coeff_a) + "x^2 + " + str(coeff_b) + 
      "x + " + str(coeff_c) + " is: ")
print(str(smaller_root(coeff_a, coeff_b, coeff_c)))

coeff_a, coeff_b, coeff_c = 1, 2, 3
print("The smaller root of " + str(coeff_a) + "x^2 + " + str(coeff_b) + 
      "x + " + str(coeff_c) + " is: ")
print(str(smaller_root(coeff_a, coeff_b, coeff_c)))

coeff_a, coeff_b, coeff_c = 2, 0, -10
print("The smaller root of " + str(coeff_a) + "x^2 + " + str(coeff_b) + 
      "x + " + str(coeff_c) + " is: ")
print(str(smaller_root(coeff_a, coeff_b, coeff_c)))


coeff_a, coeff_b, coeff_c = 6, -3, 5
print("The smaller root of " + str(coeff_a) + "x^2 + " + str(coeff_b) + 
      "x + " + str(coeff_c) + " is: ")
print(str(smaller_root(coeff_a, coeff_b, coeff_c)))


