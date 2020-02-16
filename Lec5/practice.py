# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 14:31:53 2020

@author: DELL
"""

# def get_data(aTuple):
#     """
#     aTuple, tuple of tuples (int, string)
#     Extracts all integers from aTuple and sets 
#     them as elements in a new tuple. 
#     Extracts all unique strings from from aTuple 
#     and sets them as elements in a new tuple.
#     Returns a tuple of the minimum integer, the
#     maximum integer, and the number of unique strings
#     """
#     nums = ()    # empty tuple
#     words = ()
#     for t in aTuple:
#         # concatenating with a singleton tuple
#         nums = nums + (t[0],)   
#         # only add words haven't added before
#         if t[1] not in words:   
#             words = words + (t[1],)
#     # min_n = min(nums)
#     # max_n = max(nums)
#     # unique_words = len(words)
#     return (nums,words)

# test = ((1,"a"),(2, "b"),
#         (1,"a"),(7,"b"))
# test2 = test
# g = test2[0]
# g += (6.,)
# print(g)
# test2[0] += (5,3)
# print(test)
# print(test2)

# t = (1,2,3,4,5)
# print(t[::-1])

# l = (1,2)
# l += (3,4)
# print(l) 

# a = 5
# b = 3
# a,b = b,a
# print(a,b)
# a,b,c,d = (1,2,3,4)
# b,a,d,c = a,b,c,d
# print(a,b,c,d)

s = "My name is Divyam"
l = list(s)
print(type(l[0]))