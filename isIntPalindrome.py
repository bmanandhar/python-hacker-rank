#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 06:06:38 2019

@author: bijayamanandhar
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if str(x) == str(x)[::-1]:
            
            return True 
        
        return False
    
print(Solution().isPalindrome(-121))




