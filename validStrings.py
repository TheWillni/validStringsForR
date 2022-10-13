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
MAX_N = 3
MAX_M = 3
MAX_R = 20
MAX_VAL = 20
MAX_TESTS = 20
execute = "runDPDA dpdaR "
wantValid = True

def getRandomStringValid(i):
    n = getIntInRange(MIN_N, MAX_N, True)
    m = getIntInRange(MIN_M, MAX_M, True)

    # added plus to make sure r is strictly greater than
    r = getIntInRange(((2*n) + m + 2), MAX_R, True)
    
    
    valid_string = "a"*n + "b"*r + "c"*m
    
    printResult(valid_string, n, m, r)
    return ""

def getRandomStringInvalid(i):
    n = getIntInRange(MIN_N, MAX_N, False)
    m = getIntInRange(MIN_M, MAX_M, False)

    # added plus to make sure r is strictly greater than
    r = getIntInRange(((2*n) + m + 2), MAX_R, False)

    valid_string = "a"*n + "b"*r + "c"*m
    printResult(valid_string, n, m, r)
    return ""

def printResult(string, m, n ,r):
    print("Test case where R is [", isValidR(n,m,r), "]: #", i)
    print("Generated values of (n,m,r) = (", n, ",", m, ",", r, ")")
    print ("see proof: ", (r), ">", "2*",n,"+", m,"+ 1" + "    [", r, ">", ((2*n) +m+1), "]")
    print("Valid string:")
    print(string)
    print(execute +"\"" + string +"\"" + "\n")
    
def isValidR(n, m, r): 
    if ( r > ( (2*n) + m + 1)):
        return True
    else:
        return False

def getIntInRange(minValue, maxValue, wantInRange):
    notAcceptable = True
    while (notAcceptable):
        a = random.randint(0,MAX_VAL)
        if (wantInRange):
            if (a >= minValue and a <= maxValue):
                return a
        else:
            if (not (a >= minValue and a <= maxValue)):
                return a
        
for i in (range(1,MAX_TESTS+1)):
    getRandomStringValid(i)

for i in (range(1,MAX_TESTS+1)):
    getRandomStringInvalid(i)


