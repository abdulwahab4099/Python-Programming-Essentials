"""
Comparing print vs. return - version two
Print a string from inside a function call
"""

def welcome(location):
    """
    Given a string location, print a string of the form
    "Welcome to location"
    """
    answer = "Welcome to " + location
    print(answer)


welcome("Python Scripting")