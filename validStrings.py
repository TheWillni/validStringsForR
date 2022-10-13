# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 17:32:59 2022

@author: Willni
"""

# create a random string that accept the language
# R = {a^n b^r c^m | n >= 0, m >= 1, r > 2n+m+1}

import random

MIN_N = 0
MIN_M = 1
MAX_N = 20
MAX_M = 20
MAX_R = 50

n = random.randint(MIN_N, MAX_N)
m = random.randint(MIN_M, MAX_M)

# added plus to make sure r is strictly greater than
r = random.randint( ((2*n) + m + 2), MAX_R)

valid_string = "a"*n + "b"*r + "c"*m


print("Generated values of (n,m,r) = (", n, ",", m, ",", r, ")")
print("Valid string --->", valid_string)

