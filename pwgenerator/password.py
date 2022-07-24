import string
import random

def random_number(length=10, upper=True, lower=True, numbers=True, special=True):
    letters = string.ascii_letters
    numbers = string.digits
    speical_digits = string.punctuation
    
    if upper and lower and numbers and special:
        characters = letters+numbers+speical_digits
        pw = ''.join(random.choices(characters, k=length))
        return pw
    elif upper and lower and numbers:
        characters = letters+numbers
        pw = ''.join(random.choices(characters, k=length))
        # print(pw)
        return pw
    elif upper and lower and numbers:
        characters = letters+numbers
        pw = ''.join(random.choices(characters, k=length))
        # print(pw)
        return pw
    
    
random_number()