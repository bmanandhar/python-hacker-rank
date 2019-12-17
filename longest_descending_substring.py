#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 11:21:59 2019

@author: bijayamanandhar
"""

def longest_descending_substring(s):
    print('s')
    descending_substring = ''
    temp = ''
    i = 0
    while i < len(s) - 1:
        temp = s[i]
        print(temp)
        while ord(s[i + 1]) < ord(temp[-1]):
            temp += s[i+1]
        if len(descending_substring) < len(temp):
            descending_substring = temp 
        i += 1
    return descending_substring

print(longest_descending_substring("abctsrutkjglyfb"))