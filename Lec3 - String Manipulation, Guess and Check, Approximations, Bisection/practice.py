# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 11:19:27 2020

@author: DELL
"""

# s = "Divyam"
# print(s[-1::-2])

s = "6.00 is 6.0001 and 6.0002"
new_str = ""
# new_str += s[-1]
# new_str += s[0]
# new_str += s[4::30]    
new_str += s[13:10:-1]
print(new_str)