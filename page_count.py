#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 18:18:32 2019

@author: bijayamanandhar
"""

def pageCount(n, p):
    #
    # Write your code here.
    #
    
    #If number of pages is even, add 1 to it to make it 
    if n % 2 == 0:
        n += 1
    
    
    front, back = None, None
    front = p//2
    back = (n-p)//2

    if front < back or front == back:
        return front
    else:
        return back
    
print(pageCount(6, 6))

