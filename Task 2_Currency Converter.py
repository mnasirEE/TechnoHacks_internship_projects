# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 00:11:21 2023

@author: M.Nasir

"""

'''
 Task 2 :   Currency Converter
 
            Build a program that can convert currency
            from one form to another using the latest
            exchange rates 

'''
 
def currency_convertor(from_ , to , ammount):
    # Exchange Rates of 5 Countries
    
    inr_in_pkr = 3.54195      # 1INR = 3.54195 PKR
    pkr_in_inr = 0.282330     # 1PKR = 0.282330 INR
    usd_in_pkr = 294.50149    # 1USD = 294.50149 PKR
    pkr_in_usd = 0.00339557   # 1PKR = 0.00339557 USD
    pkr_in_gbp = .0026107803  # 1PKR = .0026107803 GBP
    gbp_in_pkr = 383.027      # 1GBP = 383.027 PKR
    pkr_in_cny = .023993347   # 1PKR = .023993347 CNY
    cny_in_pkr = 41.6782      # 1CNY = 41.6782 PKR
    inr_in_usd = .012090417   # 1INR = .012090417 USD
    usd_in_inr = 82.7107      # 1USD = 82.7107 INR
    inr_in_gbp = .009591881   # 1USD = .009591881 CNY
    gbp_in_inr = 104.255      # 1GBP = 104.255 INR
    inr_in_cny = 0.88150399   # 1INR = 0.88150399 CNY
    cny_in_inr = 11.3442      # 1CNY = 11.3442 INR
    usd_in_cny = 7.2909311    # 1USD = 7.2909311 CNY
    cny_in_usd = .137157      # 1CNY = .137157 USD
    usd_in_gbp = .79334574    # 1GBP = .79334574 USD
    cny_in_gbp = .108812      # 1CNY = .108812 GBP
    gbp_in_usd = 1.26048      # 1GBP = 1.26048 USD
    gbp_in_cny = 9.19011      # 1GBP = 9.19011 CNY
    
    # Conversion From PKR to INR
    
    if (from_.lower() == "pakistan" or from_.lower() == "pkr") and (to.lower() == "india" or to.lower() == "inr"):
        conv_money = ammount * pkr_in_inr
        return conv_money
    
    # Conversion from INR to PKR
    elif (from_.lower() == "india" or from_.lower() == "inr")  and (to.lower() == "pakistan" or to.lower() == 'pkr'):
        conv_money = ammount * inr_in_pkr
        return conv_money
    
    # Conversion from PKR to USD
    elif (from_.lower() == "pakistan" or from_.lower() == "pkr") and (to.lower() == "united states" or to.lower() == "usd"):
       conv_money = ammount * pkr_in_usd
       return conv_money
    
    # Conversion from USD to PKR
    elif (from_.lower() == "united states" or from_.lower() == "usd") and (to.lower() == "pakistan" or to.lower() == "pkr"):
        conv_money = ammount * usd_in_pkr
        return conv_money
    
    # Conversion from PKR to GBP
    elif (from_.lower() == "pakistan" or from_.lower() == "pkr") and (to.lower() == "united kingdom" or to.lower() == "gbp"):
        conv_money = ammount *  pkr_in_gbp
        return conv_money
    
    # Conversion from GBP to PKR
    elif (from_.lower() == "united kingdom" or from_.lower() == "gbp")  and (to.lower() == "pakistan" or to.lower() == 'pkr'):
       conv_money = ammount * gbp_in_pkr
       return conv_money
    
    # Conversion from PKR to CNY
    elif (from_.lower() == "pakistan" or from_.lower() == "pkr") and (to.lower() == "china" or to.lower() == "cny"):
        conv_money = ammount * pkr_in_cny 
        return conv_money
    
    # Conversion from CNY to PKR
    elif (from_.lower() == "china" or from_.lower() == "cny") and (to.lower() == "pakistan" or to.lower() == "pkr"):
        conv_money = ammount * cny_in_pkr
        return conv_money
    
    # Conversion from INR to USD
    elif (from_.lower() == "india" or from_.lower() == "inr") and (to.lower() == "united states" or to.lower() == "usd"):
        conv_money = ammount * inr_in_usd
        return conv_money
    
    # Conversion from USD to INR
    elif (from_.lower() == "united states" or from_.lower() == "usd")  and (to.lower() == "india" or to.lower() == 'inr'):
       conv_money = ammount * usd_in_inr
       return conv_money
    
    # INR to GBP
    elif (from_.lower() == "india" or from_.lower() == "inr") and (to.lower() == "united kingdom" or to.lower() == "gbp"):
        conv_money = ammount * inr_in_gbp
        return conv_money
    
    # GBP to INR
    elif (from_.lower() == "united kingdom" or from_.lower() == "gbp") and (to.lower() == "india" or to.lower() == "inr"):
        conv_money = ammount * gbp_in_inr
        return conv_money
    
    # INR to CNY
    elif (from_.lower() == "india" or from_.lower() == "inr") and (to.lower() == "china" or to.lower() == "cny"):
        conv_money = ammount *  inr_in_cny
        return conv_money
    
    # CNY to INR
    elif (from_.lower() == "china" or from_.lower() == "cny")  and (to.lower() == "india" or to.lower() == 'inr'):
        conv_money = ammount * cny_in_inr
        return conv_money
    
    # USD to CNY
    elif (from_.lower() == "united states" or from_.lower() == "usd") and (to.lower() == "china" or to.lower() == "cny"):
        conv_money = ammount * usd_in_cny 
        return conv_money
    
    # CNY to USD
    elif (from_.lower() == "china" or from_.lower() == "cny") and (to.lower() == "united states" or to.lower() == "usd"):
        conv_money = ammount * cny_in_usd
        return conv_money
    
    # USD to GBP
    elif (from_.lower() == "united states" or from_.lower() == "usd")  and (to.lower() == "united kingdom" or to.lower() == 'gbp'):
        conv_money = ammount * usd_in_gbp
        return conv_money
    
    # GBP to USD
    elif (from_.lower() == "united kingdom" or from_.lower() == "gbp")  and (to.lower() == "united states" or to.lower() == 'usd'):
        conv_money = ammount * gbp_in_usd
        return conv_money
    
    # GBP to CNY
    elif (from_.lower() == "united kingdom" or from_.lower() == "gbp")  and (to.lower() == "china" or to.lower() == 'cny'):
        conv_money = ammount * gbp_in_cny
        return conv_money
    
    # CNY to GBP
    elif (from_.lower() == "china" or from_.lower() == "cny") and (to.lower() == "united kingdom" or to.lower() == 'gbp'):
        conv_money = ammount * cny_in_gbp 
        return conv_money
    
    # If Both currencies are same
    elif from_.lower() == to.lower():
       return ammount
    
        
    

    
list_of_countries = ['Pakistan', 'India', 'United States', 'United Kingdom', 'China']
print("*** Enter Country Name or Currency Name according to the given country list: ***\n",list_of_countries,"\n")
from_ = input("Convert Currency from: ")
to = input("Convert Currency To: ")
ammount = float(input("Now Enter ammount: "))
print(f"{ammount} {from_} is equal to" ,currency_convertor(from_, to, ammount), to)
