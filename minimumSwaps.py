#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 13:58:52 2019

@author: bijayamanandhar
"""
"""
You are given an unordered array consisting of consecutive 
integers  [1, 2, 3, ..., n] without any duplicates. You are
 allowed to swap any two elements. You need to find the minimum
 number of swaps required to sort the array in ascending order.

For example, given the array  we perform the following steps:

i   arr                         swap (indices)
0   [7, 1, 3, 2, 4, 5, 6]   swap (0,3)
1   [2, 1, 3, 7, 4, 5, 6]   swap (0,1)
2   [1, 2, 3, 7, 4, 5, 6]   swap (3,4)
3   [1, 2, 3, 4, 7, 5, 6]   swap (4,5)
4   [1, 2, 3, 4, 5, 7, 6]   swap (5,6)
5   [1, 2, 3, 4, 5, 6, 7]
It took  swaps to sort the array.

Function Description

Complete the function minimumSwaps in the editor below.
It must return an integer representing the minimum number
of swaps to sort the array.

minimumSwaps has the following parameter(s):

arr: an unordered array of integers
Input Format

The first line contains an integer, , the size of .
The second line contains  space-separated integers .

Constraints

Output Format

Return the minimum number of swaps to sort the given array."""

class Solution:
    
    def minimumSwaps(self, arr):
        
        arr = [i-1 for i in arr]
        
        swap = i = 0
        
        while i < len(arr):
            if arr[i] == i:
                i += 1
                continue
            arr[arr[i]], arr[i] = arr[i], arr[arr[i]]
            
            swap += 1
            
        return swap

if __name__=='__main__':
    
    S = Solution()
    
    print(S.minimumSwaps([4,3,1,6,2,5]))
    
    
    