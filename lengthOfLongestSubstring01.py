#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 17:23:28 2019

@author: bijayamanandhar
"""
from datetime import datetime

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r, max_len = 0, 1, 0
        
        while r < len(s):
            max_len = max(max_len, len(s[l:r]))
            while s[r] in s[l:r]:
                l += 1
            r += 1
        
        return max(max_len, len(s[l:r]))
            
if __name__ == '__main__':
    S = Solution()
    start = datetime.now()
    print(start)
    print(S.lengthOfLongestSubstring(
        """abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\
        "#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\
        "#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\
        "#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\
        "#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\
        "#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\
        "#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\
        "#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\
        "#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\
        "#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\
        "#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ abcdefghijklmnopqrstuvwxyzABC"""
        )
    )
    end = datetime.now()
    print(end)    

    print(S.lengthOfLongestSubstring("""abcabcbb""")==3)
    print(S.lengthOfLongestSubstring("pwwkew")==3)
    print(S.lengthOfLongestSubstring("bbbb")==1)
    print(S.lengthOfLongestSubstring("dvdf")==3)
    print(S.lengthOfLongestSubstring("b")==1)
    print(S.lengthOfLongestSubstring("as")==2)
    print(S.lengthOfLongestSubstring("")==0)
    print(S.lengthOfLongestSubstring("abcdefghijklmnopqrstuvwxyz")==26)
    print(S.lengthOfLongestSubstring("abcdefghijklxxmnopqrstuvwxyz")==14)









