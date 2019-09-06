#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 13:38:51 2019

@author: bijayamanandhar
"""

"""
#01
def findNumber(arr, k):
  if k in arr:
    print("Yes!")
  else: print("No!")
findNumber([1,2,3,4], 0)


#02
def oddNumbers(l, r):
    
    for i in range(l, r+1):
        if i % 2 != 0:
            print(i)
oddNumbers(1, 9)
    

a = [0,2,3,2]
a.remove(a[2])
print(a)
"""
"""
#03
def sockMerchant(n, ar):

    set_ar = set(ar)
    total_pairs = 0
    
    for i in set_ar:
        piece = 0
        for j in ar:
            if i == j:
                piece += 1
                if piece == 2:
                    total_pairs += 1
                    piece = 0
    return total_pairs
                    
print(sockMerchant(9, [1,2,0,1,3,1,3,0,9,4,4,9]))

#04
#Num of valleys

def countingValleys(n, s):
    num_valleys = 0 # no. of valleys
    level = 0 # starts at sea-level
    for d in s:
        if d == 'U': # steps uphill
            level += 1
        else:
            if level == 0:
                num_valleys += 1
            level -= 1
    return num_valleys

#05
# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):  
    current = 0
    end = len(c) - 1
    jumps = 0
    while current < end:
        if ((current + 2) <= end) and (c[current + 2] == 0):
            current += 2
            jumps += 1
        elif c[current + 1] == 0:
            current += 1
            jumps += 1
    return jumps  

#06
# Complete the repeatedString function below.
def repeatedString(s, n):
    string = ""
    while len(string) < n:
        string += s

    string = string[:n]

    return string.count('a')
print(repeatedString("aba", 10))


#07
# Complete the simpleArraySum function below.
#
def simpleArraySum(ar):
    #
    # Write your code here.
    #
    if len(ar) > 1000:
        return False
    sum = 0

    for i in ar:
        sum += i
    return sum 

#08
# Complete the compareTriplets function below.
def compareTriplets(a, b):
    alice, bob = 0, 0

    for i in range(3): 
        if a[i] > b[i]: alice += 1
        if a[i] < b[i]: bob += 1
    
    return [alice, bob]

# Complete the aVeryBigSum function below.
def aVeryBigSum(ar):
    sum = 0
    for i in ar: sum += i
    return sum 

#09
#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

#10
def diagonalDifference(arr):
    # Write your code here
    
    primary, secondary = 0, 0
    for i in range(len(arr)):
        primary += arr[i][i] 
        secondary += arr[len(arr)-1-i][i]
    return abs(primary - secondary)


#11
# Complete the plusMinus function below.
def plusMinus(arr):

    positive, neutral, negative = 0, 0, 0
    num = len(arr)
    for i in arr: 
        if i > 0: positive += 1
        elif i < 0: negative += 1
        else: neutral += 1 
    print(positive/num)
    print(negative/num)
    print(neutral/num)
    """
#12
# Complete the staircase function below.
def staircase(n):
    string = ""
    for i in range(n):
        string += " "*(n-i-1) + "#"*(i+1)
        print (string)
        string = ""


#13
# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    sum, sum_arr = 0, []
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i != j: sum += arr[j]
        sum_arr.append(sum)
        sum = 0
    print(min(sum_arr), max(sum_arr))

#14
    
# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    tallest_candle_height = max(ar)
    total_tallest_candles = 0
    for candle_height in ar: 
        if candle_height == tallest_candle_height:
            total_tallest_candles += 1
    return total_tallest_candles
    

#15


#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #
    military_time = ''

    if s[-2] == 'A':
        if s[0:2] == '12':
            military_time = '00' + s[2:-2]
        else:
            military_time = s[0:-2]
    else:
        if s[0:2] == 12:
            military_time = str(int(s[0:2])) + s[2:-2]
        else:
            military_time = str((int(s[0:2]) + 12)%24) + s[2:-2]
    return military_time
print(timeConversion("12:34:04PM"))

#16

x = "bijaya"
print(x[1:-2])

#17

#18

#19

#20    



