"""
Compute the statement about a person's name and age, given the person's name and age.
"""

###################################################
# Name and age formula

def name_and_age(name, age):
    """
    Compute the statement about a person's name and age, given the person's name and age.
    """
    if age < 0:
        return "Error: Invalid age"
    else:
        return name + " is " + str(age) + " years old."
    




###################################################
# Tests


name, age = "Abdul Wahab", 21
print(name_and_age(name, age))

name, age = "Ahsan Ali", 20
print(name_and_age(name, age))

name, age = "Joe Warren", 56
print(name_and_age(name, age))

name, age = "Scott Rixner", 40
print(name_and_age(name, age))

name, age = "John Greiner", -46
print(name_and_age(name, age))



