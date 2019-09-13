#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 22:32:30 2019

@author: bijayamanandhar
"""
#Github repo: 
#https://www.hackerrank.com/challenges/divisible-sum-pairs/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign

"""

You are given an array of  integers, , and a positive integer, . Find and print the number of  pairs where  and  +  is divisible by .

For example,  and . Our three pairs meeting the criteria are  and .

Function Description

Complete the divisibleSumPairs function in the editor below. It should return the integer count of pairs meeting the criteria.

divisibleSumPairs has the following parameter(s):

n: the integer length of array 
ar: an array of integers
k: the integer to divide the pair sum by
Input Format

The first line contains  space-separated integers,  and .
The second line contains  space-separated integers describing the values of .

Constraints

Output Format

Print the number of  pairs where  and  +  is evenly divisible by .

Sample Input

6 3
1 3 2 6 1 2
Sample Output

 5
Explanation

Here are the  valid pairs when :


"""




#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    
    #collects number of pairs
    res = 0;
    
    #iterates thru the length - 1
    for i in range(n-1):
        
        #iterates from i+1 to length, searches for the pairs 
        for j in range(i+1, n):
            
            #when sum equals k
            if (ar[i] + ar[j]) % k == 0:
                
                #adds 1 to res
                res += 1
            
    return res


# Test Cases:
n = 5
k = 3
ar = [1,2,3,4,1,3,0]
print(divisibleSumPairs(n, k, ar) == 3) 
# True ([ar[0]+ar[1]] = 3)\\//([ar[1]+ar[3] = 3)\\//([ar[1]+ar[4] = 3)


