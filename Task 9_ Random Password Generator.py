
"""
Created on Sun Aug 20 00:17:47 2023

@author: vc
"""

'''Task 9 : Random Password Generator
Create a program that generates a random
password of a user-defined length'''

import random
pass_length = int(input("Enter length of your password: "))
password = ""

for i in range (pass_length):
   
    string_of_password_characters = """abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
    l = random.choice(string_of_password_characters)
    password = password + l
print("Your Random Stron Password is: ",password)    