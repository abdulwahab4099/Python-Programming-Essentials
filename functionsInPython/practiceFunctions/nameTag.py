"""
Compute a name tag, given the first and last name.
"""

###################################################
# Name tag formula


def name_tag(first_name, last_name):
    """
    Compute a name tag, given the first and last name.
    """
    return "My name is " + first_name + " " + last_name


    
###################################################
# Tests

    
    
first_name, last_name = "Abdul", "Wahab"
print(name_tag(first_name, last_name))

first_name, last_name = "Ahsan", "Ali"
print(name_tag(first_name, last_name))

first_name, last_name = "Khizar", "Mirza"
print(name_tag(first_name, last_name))


