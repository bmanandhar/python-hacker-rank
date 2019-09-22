#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 21:18:52 2019

@author: bijayamanandhar
"""

"""
A left rotation operation on an array shifts each of the array's elements  unit to the left. For example, if  left rotations are performed on array , then the array would become .

Given an array  of  integers and a number, , perform  left rotations on the array. Return the updated array to be printed as a single line of space-separated integers.

Function Description

Complete the function rotLeft in the editor below. It should return the resulting array of integers.

rotLeft has the following parameter(s):

An array of integers .
An integer , the number of rotations.
Input Format

The first line contains two space-separated integers  and , the size of  and the number of left rotations you must perform.
The second line contains  space-separated integers .

Constraints

Output Format

Print a single line of  space-separated integers denoting the final state of the array after performing  left rotations.

Sample Input

5 4
1 2 3 4 5
Sample Output

5 1 2 3 4
Explanation

When we perform  left rotations, the array undergoes the following sequence of changes:


"""
def rotLeft(a, d):

    #Moving d number of elements to its left
    #It's the same as moving the remaining elements to its right
    #Slice the array into left and right portions 
    #Concatenate in reverse order
       
    return a[d:len(a)] + a[:d]
    
print(rotLeft([1,2,3,4,5], 4) == [5, 1, 2, 3, 4]) #Prints 'True'
    
    
    
