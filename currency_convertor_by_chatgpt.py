# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 00:12:08 2023

@author: vc
"""

from forex_python.converter import CurrencyRates

def get_conversion_rate(from_currency, to_currency):
    c = CurrencyRates()
    return c.get_rate(from_currency, to_currency)

def convert_currency(amount, from_currency, to_currency):
    conversion_rate = get_conversion_rate(from_currency, to_currency)
    converted_amount = amount * conversion_rate
    return converted_amount

def main():
    print("Currency Converter")
    print("------------------")

    amount = float(input("Enter the amount: "))
    from_currency = input("Enter the source currency: ").upper()
    to_currency = input("Enter the target currency: ").upper()

    converted_amount = convert_currency(amount, from_currency, to_currency)

    print(f"{amount:.2f} {from_currency} is equivalent to {converted_amount:.2f} {to_currency}")

if __name__ == "__main__":
    main()
