"""
Demonstration of defining functions.
"""

def sayhello():
    """
    Prints "hello".
    """
    print("hello world")

# Call the function
sayhello()

def double(value):
    """
    Return twice the input value
    """
    return value * 2

# Call the function and assign the result to a variable
result = double(56)
print(result)

def product(value1, value2, value3):
    """
    Returns the product of the three input values.
    """
    prod = value1 * value2 * value3
    
    return prod

# Call the function and assign the result to a variable
result = product(7, 15, -12)
print(result)
