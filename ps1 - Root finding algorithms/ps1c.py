# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 12:03:56 2020

@author: DELL
"""

annual_salary = float(input("Enter the starting salary: "))
semi_annual_raise = 0.07
down_payment = 0.25 * 1000000
annual_return_on_saving = 0.04


def money_saved(portion_saved):
    current_savings = 0
    monthly_salary = annual_salary/12.0
    portion_saved /= 10000
    for months in range(36):
        current_savings += current_savings*annual_return_on_saving/12.0 + monthly_salary*portion_saved
        months += 1
        if(months % 6 == 0):
            monthly_salary *= 1.0 + semi_annual_raise
            
    return current_savings

low = 0
high = 10000
guess = (low+high)/2
steps = 1
while(abs(money_saved(guess)-down_payment) > 100):
    money = money_saved(guess)
    if(money < down_payment):
        low = guess
    else:
        high = guess
    guess = int((low+high)/2)
    steps += 1
    if(steps == 14):
        break

if(steps < 14):
    print("Best savings sate:", guess/10000)
    print("Steps in bisection search:", steps)
else:
    print("It is not possible to pay the down payment in three years.")
