import string
import random

# set global variables for the password characters
lower_letters = string.ascii_lowercase
upper_letters = string.ascii_uppercase
numbers = string.digits
special_char = string.punctuation

def get_password(length = 0, upper = True, lower = True, numb = True, spec = True):
    '''
    
    '''
    # set an empty password string
    pw = '' 
    
    # check to see if uppercase letters was selected
    if upper: 
        pw += upper_letters
    
    # check to see if lowercase letters was selected
    if lower:
        pw += lower_letters
    
    # check to see if numbers were selected
    if numb:
        pw += numbers
    
    # check to see if special characters were selected
    if spec:
        pw += special_char
    
    # take the new password then randomize the choices, and join them, with the selected length
    pw = ''.join(random.choices(pw, k=length))
    # print(pw)
    return pw

get_password()