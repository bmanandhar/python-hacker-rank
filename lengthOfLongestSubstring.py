#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 09:22:04 2019

@author: bijayamanandhar
"""
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        # Case: when string length is 0 or 1
        if len(s) <= 1: return len(s)
        
        # Assume the longest length
        
        longestLength = 0
        
        # iterate thru the string for each element
        
        for i in range(len(s)):
            
            # helper to find longest length for specific element
            lengthChecked = self.helper(s[i:])
            if longestLength < lengthChecked:
                longestLength = lengthChecked
        
        return longestLength
            
    def helper(self, x):
        
        # for specific element
        strLength, tempStr = 0, x[0]
        
        # check for longest length
        for i in range(1, len(x)):
            
            if x[i] not in tempStr:
                tempStr += x[i]
                    
                if strLength < len(tempStr):
                    strLength = len(tempStr)
          
            elif x[i] in tempStr:
                if strLength < len(tempStr):
                    strLength = len(tempStr)
                tempStr = x[i]
                
        return strLength    

if __name__ == '__main__':
    S = Solution()
    
    print(S.lengthOfLongestSubstring("abcabcbb"))
    print(S.lengthOfLongestSubstring("pwwkew"))
    print(S.lengthOfLongestSubstring("bbbb"))
    print(S.lengthOfLongestSubstring("dvdf"))
    print(S.lengthOfLongestSubstring("abcdefghijklmnopqrstuvwxyz"))
 