"""
Compute the statement about a person's name and age, given the person's name and age.
"""

###################################################
# Name and age formula

def name_and_age(name, age):
    return name + " is " + str(age) + " years old."



###################################################
# Tests


    
name, age = "Abdul Wahab", 21
print(name_and_age(name, age))

name, age = "Ahsan Ali", 20
print(name_and_age(name, age))

name, age = "Khizar Mirza", 20
print(name_and_age(name, age))



