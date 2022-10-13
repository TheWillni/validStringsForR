# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 17:32:59 2022

@author: Willni
"""

# create a random string that accept the language
# R = {a^n b^r c^m | n >= 0, m >= 1, r > 2n+m+1}

import random
import math

MIN_N = 0
MIN_M = 1
MAX_N = 3
MAX_M = 3
MAX_R = 20
MAX_VAL = 20
MAX_TESTS = 15
execute = "runDPDA dpdaR "
wantValid = True

def getRandomStringValid(i):
    n = getIntInRange(MIN_N, MAX_N, True)
    m = getIntInRange(MIN_M, MAX_M, True)

    # added plus to make sure r is strictly greater than
    r = getIntInRange(((2*n) + m + 2), MAX_R, True)
    
    
    valid_string = "a"*n + "b"*r + "c"*m
    
    printResult(valid_string,i)
    return ""

def getRandomStringInvalid(i):
    n = getIntInRange(MIN_N, MAX_N, False)
    m = getIntInRange(MIN_M, MAX_M, False)

    # added plus to make sure r is strictly greater than
    r = getIntInRange(((2*n) + m + 2), MAX_R, False)

    valid_string = "a"*n + "b"*r + "c"*m
    printResult(valid_string,i)
    return ""
def swapRandomly(string):
    
    if len(string) < 6:
        return string
    min_index = 0
    max_index = len(string)
    max_len = math.floor(max_index/3)
    
    #pick a random substring of length 2,(1/3 len) in the first half of string
    first_len = random.randint(2,max_len)
    first_start = random.randint(min_index, (math.floor((max_index)/2 - first_len)))
    # pick a random substring of length 2-5 in second half
    second_len = random.randint(2,max_len)
    second_start = random.randint(math.floor(max_index/2), max_index - second_len)
    
    start = string[:first_start]
    first_sub = string[first_start:(first_start + first_len)]
    middle = string[(first_start + first_len):(second_start)]
    second_sub = string[(second_start):(second_start + second_len)]
    end = string[(second_start + second_len):]
    
    final = start + second_sub + middle + first_sub + end
    return final
    
        
    return string
def getRandomStringInvalidOrder(i):
    count = 0
    n = getIntInRange(MIN_N, MAX_N, True)
    m = getIntInRange(MIN_M, MAX_M, True)

    # added plus to make sure r is strictly greater than
    r = getIntInRange(((2*n) + m + 2), MAX_R, True)

    valid_string = "a"*n + "b"*r + "c"*m
    while (isValidR(valid_string)):
           valid_string = swapRandomly(valid_string)
           if (count > 10): 
               # force a instant exception if we fail to randomly ruin order
               # randomly
               valid_string = "cb" + valid_string
           count += 1
    printResult(valid_string, i)
    return ""

def printResult(string, i):
    n = string.count('a')
    m = string.count('c')
    r = string.count('b')
    print(f"Test case: # {i}")
    print("Generated values of (n,m,r) = (", n, ",", m, ",", r, ")")
    print (f"see guard: {r} > 2*{n} + {m} + 1    [{r} > { (2*n) + m + 1}]")
    #print(string)
    print("\n" + execute +"\"" + string +"\"")
    print(f"expected output: {getOutput(string)}\n\n")
    
def isValidR(string): 
    if (not (isOrderedString(string))):
        return False
    n = string.count('a')
    m = string.count('c')
    r = string.count('b')
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
def getOutput(string):
    if (isValidR(string)):
        return "accept"
    return "reject"

def remove_consec_duplicates(s):
    new_s = ""
    prev = ""
    for c in s:
        if len(new_s) == 0:
            new_s += c
            prev = c
        if c == prev:
            continue
        else:
            new_s += c
            prev = c
    return new_s

def isOrderedString(string):
    removed_dupes = remove_consec_duplicates(string)
    if (removed_dupes == "a" or 
        removed_dupes == "ab" or 
        removed_dupes == "abc" or
        removed_dupes == "b" or
        removed_dupes == "bc" or
        removed_dupes == "c"
        ):
        return True
    return False

print("There are 3 categories of tests (15 each): ")
print("    -ACCEPT STATES")
print("    -REJECT STATES (correct order, false condition)")
print("    -REJECT STATES (incorrect order, true condition)\n\n")

print("#"*10 + "--ACCEPT STATES--" + "#"*10 + "\n")
for i in (range(1,MAX_TESTS+1)):
    getRandomStringValid(i)

print("\n"* 10 +"#"*10 + "--REJECT STATES (correct order, false condition)--" + "#"*10 + "\n")
for i in (range(1,MAX_TESTS+1)):
    getRandomStringInvalid(i + MAX_TESTS)
    
print("\n"* 10 +"#"*10 + "--REJECT STATES (incorrect order, true condition)--" + "#"*10 + "\n")
for i in (range(1,MAX_TESTS+1)):
    getRandomStringInvalidOrder(i + (MAX_TESTS*2))



