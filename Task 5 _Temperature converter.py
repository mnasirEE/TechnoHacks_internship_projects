# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 00:14:53 2023

@author: M.Nasir

"""

'''
Task 5 :   Temperature converter

           Create a program that allows the user to
           convert temperatures between Fahrenheit and
           Celsius. 
'''

# Formulas

# °F = °C * 9/5 + 32
# °C = (°F - 32) * (5/9)
# °K = °C + 273.15
# °C = °K - 273.15
# °F = (°K – 273.15) × 9 ⁄ 5 + 32
# °K =  (°F - 32) * (5/9) + 273.15

# This is the Function to convert temperature from one scale to another

def temp_convertor(from_, to, temp):
    
    # Convert from celcius to fehrenheit
    if from_.lower() == "c" and to.lower() == 'f':
       con_temp = (temp * (9/5)) + 32
       return con_temp
    
    # Convert from Fehrenheit to Celcius
    elif from_.lower() == "f" and to.lower() == 'c':
        con_temp = (temp - 32) * (5/9)
        return con_temp
    
    # Convert from Celcius to Kelvin
    elif from_.lower() == 'c' and to.lower() == 'k':
        con_temp = temp + 273.15
        return con_temp
    
    # Convert from Kelvin to Fehrenheit
    elif from_.lower() == 'k' and to.lower() == 'c':
        con_temp = temp - 273.15
        return con_temp
    
    # Convert from Kelvin to Fehrenheit
    elif from_.lower() == 'k' and to.lower() == 'f':
        con_temp = ((temp - 273.15) * (9/5)) + 32
        return con_temp
    
    # Convert from Fehrenheit to Kelvin
    elif from_.lower() == 'f' and to.lower() == 'k':
        con_temp = ((temp - 32)* (5/9)) + 273.15
        return con_temp
        


print("*** Enter 'F' for Fehrenheit, 'C' for Celcius, 'K' for Kelvin ***\n")
from_ = input("Convert Temperature from: ") # Enter Temperature scale to be converted
to = input("Convert Temperature to: ")      # Enter Tempecature scale in which you want to convert
temp = float(input("Enter ammount of Temperature: ")) # Enter ammount of Temperature
# Here is Function call that converts temperature according to your required scale
print(f"{temp} °{from_.upper()} is equal to", temp_convertor(from_, to, temp), f"°{to.upper()}") 

