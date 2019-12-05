#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 14:41:49 2019

@author: bijayamanandhar
"""
"""
Starting with a 1-indexed array of zeros and a list of operations,
 for each operation add a value to each of the array element between
 two given indices, inclusive. Once all operations have been performed,
 return the maximum value in your array.

For example, the length of your array of zeros . 
Your list of queries is as follows:

    a b k
    1 5 3
    4 8 7
    6 9 1
Add the values of  between the indices  and  inclusive:

index->	 1 2 3  4  5 6 7 8 9 10
	[0,0,0, 0, 0,0,0,0,0, 0]
	[3,3,3, 3, 3,0,0,0,0, 0]
	[3,3,3,10,10,7,7,7,0, 0]
	[3,3,3,10,10,8,8,8,1, 0]
The largest value is  after all operations are performed.

Function Description

Complete the function arrayManipulation in the editor below. It must return an integer, the maximum value in the resulting array.

arrayManipulation has the following parameters:

n - the number of elements in your array
queries - a two dimensional array of queries where each queries[i] contains three integers, a, b, and k.
Input Format

The first line contains two space-separated integers  and , the size of the array and the number of operations.
Each of the next  lines contains three space-separated integers ,  and , the left index, right index and summand.

Constraints

Output Format

Return the integer maximum value in the finished array.

Sample Input

5 3
1 2 100
2 5 100
3 4 100
Sample Output

200
Explanation

After the first update list will be 100 100 0 0 0.
After the second update list will be 100 200 100 100 100.
After the third update list will be 100 200 200 200 100.
The required answer will be .
"""


# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):

    # create a list of zeros with n as its length    
    num = [0] * n

    # iterate the list for number of times equal to the length of queries list
    for i in range(len(queries)):

        # iterate the list thru lower and higher indices shown by queries
        for j in range(queries[i][0]-1, queries[i][1]):

            # add and adder-value of queries to the elements
            num[j] = num[j] + queries[i][2]

    # select the highes value of elements after all operations are done
    return max(num)


