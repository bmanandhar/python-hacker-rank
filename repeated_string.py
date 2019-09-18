#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 18:00:31 2019

@author: bijayamanandhar
"""

"""
Lilah has a string, , of lowercase English letters that she repeated infinitely many times.

Given an integer, , find and print the number of letter a's in the first  letters of Lilah's infinite string.

For example, if the string  and , the substring we consider is , the first  characters of her infinite string. There are  occurrences of a in the substring.

Function Description

Complete the repeatedString function in the editor below. It should return an integer representing the number of occurrences of a in the prefix of length  in the infinitely repeating string.

repeatedString has the following parameter(s):

s: a string to repeat
n: the number of characters to consider
Input Format

The first line contains a single string, .
The second line contains an integer, .

Constraints

For  of the test cases, .
Output Format

Print a single integer denoting the number of letter a's in the first  letters of the infinite string created by repeating  infinitely many times.

Sample Input 0

aba
10
Sample Output 0

7
Explanation 0
The first  letters of the infinite string are abaabaabaa. Because there are  a's, we print  on a new line.

Sample Input 1

a
1000000000000
Sample Output 1

1000000000000
Explanation 1
Because all of the first  letters of the infinite string are a, we print  on a new line.

"""


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.

def repeatedString(s, n):
    
    # number of full strings to make the length equal to n
    number_of_strings = n//len(s)
    
    # extra length that does not cover the full length os s
    remainder = n % len(s)
    
    # count1, number of 'a' in the length divisible by n
    # count2, number of 'a' in the remainder length
    count1, count2 = 0, 0 
    
    # counting a
    for i in range(len(s)):
        
        # number of a in the original string
        if s[i] == 'a':
            count1 += 1
            
        # number of a in the extra length
        if s[i] == 'a' and i < remainder:
            count2 += 1
            
    return count1 * number_of_strings + count2
    
        
#Program ends here    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()