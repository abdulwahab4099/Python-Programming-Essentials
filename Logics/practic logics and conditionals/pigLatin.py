"""
Compute a (simplified) Pig Latin version of a word.
"""

###################################################
# Pig Latin function
def pig_latin(word):
    """
    Returns the (simplified) Pig Latin version of the word.
    """

    # Partial code for body
    first_letter = word[0]
    rest_of_word = word[1 : ]

    
    
    if first_letter.lower() in "aeiou":
        return word + "way"
    else:
        return rest_of_word + first_letter + "ay"
    
    
    

###################################################
# Tests

    
word = "pig"
print(pig_latin(word))

word = "owl"
print(pig_latin(word))

word = "python"
print(pig_latin(word))


