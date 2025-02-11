"""
Comparing print vs. return - version three
Print a string from inside a function call and
erroneously also print the returned result
"""

def welcome(location):
    """
    Given a string location, print a string of the form
    "Welcome to location"
    """
    answer = "Welcome to " + location
    print(answer)


print(welcome("Python Scripting"))