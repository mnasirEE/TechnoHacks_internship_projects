
"""
Created on Sun Aug 20 00:17:47 2023

@author: M.Nasir
"""

'''Task 9 : Random Password Generator
Create a program that generates a random
password of a user-defined length'''

import random
import string as str

def random_password_generator(pass_length = 12, uppercase = 1, special_chars = 1, digits = 1):

    capital_letters = str.ascii_uppercase
    lower_letters = str.ascii_lowercase
    characters = str.punctuation
    numbers = str.digits
   
    password = list( ''.join(random.choice(capital_letters) for i in range(uppercase)) +
                     ''.join(random.choice(characters) for j in range(special_chars)) +
                     ''.join(random.choice(numbers) for k in range(digits)) +
                     ''.join(random.choice( capital_letters + lower_letters + characters + numbers)
                     for l in range( pass_length - uppercase - digits - special_chars)))
   
    random.shuffle(password)
    final_password = ''.join(password)
    return final_password

pass_length = int(input("Enter length of your password: "))
uppercase = int(input("Enter minimum number of capital letters: "))
special_chars = int(input("Enter minimum number of special characters: "))
digits = int(input("Enter minimum number of digits: "))
print("Random Password is: ",random_password_generator(pass_length, uppercase, special_chars, digits))    
