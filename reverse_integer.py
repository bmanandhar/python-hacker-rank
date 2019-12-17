#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 22:32:21 2019

@author: bijayamanandhar
"""

class Solution:
    def reverse(self, x: int) -> int:
        
        if x >= 0: 
            string = str(int(str(abs(x))[::-1]))
            
        else:
            string = '-' + str(int(str(abs(x))[::-1]))
                
        if int(string) <= -2**31 or int(string) >= 2**31-1:
            return 0
        
        return string
            
"""Runtime: 32 ms, faster than 81.21% of Python3 online
 submissions for Reverse Integer. Memory Usage: 12.8 MB, 
 less than 100.00% of Python3 online submissions for 
 Reverse Integer."""
 
 class Solution:
    def reverse(self, x: int) -> int:
        rev = (-1) ** (x<0) * int(''.join(list(str(abs(x)))[::-1]))
        rev = rev if (rev >= (-2)**31) & (rev <= 2**31-1) else 0
        return rev
    
    
    
    
    
    
    
    