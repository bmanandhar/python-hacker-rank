#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 18:18:32 2019

@author: bijayamanandhar
"""

"""
Brie’s Drawing teacher asks her class to open their books to a page number. Brie can either start turning pages from the front of the book or from the back of the book. She always turns pages one at a time. When she opens the book, page  is always on the right side:

image

When she flips page , she sees pages  and . Each page except the last page will always be printed on both sides. The last page may only be printed on the front, given the length of the book. If the book is  pages long, and she wants to turn to page , what is the minimum number of pages she will turn? She can start at the beginning or the end of the book.

Given  and , find and print the minimum number of pages Brie must turn in order to arrive at page .

Function Description

Complete the pageCount function in the editor below. It should return the minimum number of pages Brie must turn.

pageCount has the following parameter(s):

n: the number of pages in the book
p: the page number to turn to
Input Format

The first line contains an integer , the number of pages in the book.
The second line contains an integer, , the page that Brie's teacher wants her to turn to.

Constraints

Output Format

Print an integer denoting the minimum number of pages Brie must turn to get to page .

Sample Input 0

6
2
Sample Output 0

1
Explanation 0

If Brie starts turning from page , she only needs to turn  page:
"""


def pageCount(n, p):
    #
    # Write your code here.
    #
    
    #If number of pages is even, add 1
    if n % 2 == 0:
        n += 1
    
    front, back = None, None
    
    
    #Number of pages to turn from front
    #Turning pages from front has nothing to do with total pages
    #Because it starts from page-1
    front = p//2

    #Number of pages to turn from back    
    back = (n-p)//2

    #Check which is smaller
    if front < back or front == back:
        return front
    
    else:
        return back
    
print(pageCount(6, 5) == 1)#Prints 'True'

