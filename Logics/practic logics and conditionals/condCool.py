"""
Compute whether a person is cool.
"""

###################################################
# Is cool formula

def is_cool(name):
    return name == "Joe" or name == "John" or name == "Stephen"






###################################################
# Tests


name = "Joe"
if is_cool(name):
    print(name, "is cool.")
else:
    print(name, "is not cool.")

name = "John"
if is_cool(name):
    print(name, "is cool.")
else:
    print(name, "is not cool.")
    
name = "Stephen"
if is_cool(name):
    print(name, "is cool.")
else:
    print(name, "is not cool.")
    
name = "Scott"
if is_cool(name):
    print(name, "is cool.")
else:
    print(name, "is not cool.")

