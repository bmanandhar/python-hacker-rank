#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 21:18:52 2019

@author: bijayamanandhar
"""


def rotLeft(a, d):

    #Creates a variable for the result
    result = []

    #Moving the elements to its left in a new array     
    for i in range(0, d):
        
        result.append(a[i])
        
    return a[(d):len(a)] + result
    
    
    
print(rotLeft([1,2,3,4,5], 4) == [5, 1, 2, 3, 4]) #Should print 'True'
    
    
    
