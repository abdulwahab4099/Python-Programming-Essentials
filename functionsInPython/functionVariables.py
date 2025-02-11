"""
Demonstration of parameters and variables within functions.
"""

def fahrenheit_to_celsius(fahrenheit):
    """
    Return celsius temperature that corresponds to fahrenheit
    temperature input.
    """
    offset = 32
    multiplier = 5 / 9
    celsius = (fahrenheit - offset) * multiplier
    print("inside function:", fahrenheit, offset, multiplier, celsius)
    return celsius

temperature = 98.6
converted = fahrenheit_to_celsius(temperature)
print("Fahrenheit temp:", temperature)
print("Celsius temp:", converted)

# Variables defined inside a function are local to that function
fahrenheit = 37
offset = 2
multiplier = 19
celsius = 77
print("before:", fahrenheit, offset, multiplier, celsius)
newtemp = fahrenheit_to_celsius(42)
print("after:", fahrenheit, offset, multiplier, celsius)
print("result:", newtemp)
