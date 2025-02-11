"""
Comparing print vs. return - version one
Return a string from a function that is printed outside the function
"""

def welcome(location):
    """
    Given a string location, return a string of the form
    "Welcome to location"
    """
    answer = "Welcome to " + location
    return answer


print(welcome("the Matrix"))