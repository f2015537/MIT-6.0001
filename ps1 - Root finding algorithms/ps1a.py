# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 11:29:09 2020

@author: DELL
"""

annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
portion_down_payment = 0.25
current_savings = 0.0
annual_return_on_saving = 0.04
monthly_salary = annual_salary / 12.0

months = 0
while current_savings < total_cost*portion_down_payment:
    current_savings += current_savings*annual_return_on_saving/12.0 + monthly_salary*portion_saved
    months += 1

print("Number of months:",months)