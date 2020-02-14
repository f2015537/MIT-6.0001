# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 19:49:04 2020

@author: DELL
"""

# x = 5*3
# print(x)
# y = 7*8
# print(y)

# import random
# print(random.randint(1,100))


g = 1
answer = 16
iteration = 1

while abs(g*g-answer) > 0.7:
    g = (g + answer/g)/2
    print("Value= " +str(g))
    print("iteration= "+str(iteration))
    iteration += 1
    
