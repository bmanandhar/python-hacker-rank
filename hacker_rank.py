#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 13:38:51 2019

@author: bijayamanandhar
"""

"""
#01
def findNumber(arr, k):
  if k in arr:
    print("Yes!")
  else: print("No!")
findNumber([1,2,3,4], 0)


#02
def oddNumbers(l, r):
    
    for i in range(l, r+1):
        if i % 2 != 0:
            print(i)
oddNumbers(1, 9)
    

a = [0,2,3,2]
a.remove(a[2])
print(a)
"""
"""
#03
def sockMerchant(n, ar):

    set_ar = set(ar)
    total_pairs = 0
    
    for i in set_ar:
        piece = 0
        for j in ar:
            if i == j:
                piece += 1
                if piece == 2:
                    total_pairs += 1
                    piece = 0
    return total_pairs
                    
print(sockMerchant(9, [1,2,0,1,3,1,3,0,9,4,4,9]))

#04
#Num of valleys

def countingValleys(n, s):
    num_valleys = 0 # no. of valleys
    level = 0 # starts at sea-level
    for d in s:
        if d == 'U': # steps uphill
            level += 1
        else:
            if level == 0:
                num_valleys += 1
            level -= 1
    return num_valleys

#05
# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):  
    current = 0
    end = len(c) - 1
    jumps = 0
    while current < end:
        if ((current + 2) <= end) and (c[current + 2] == 0):
            current += 2
            jumps += 1
        elif c[current + 1] == 0:
            current += 1
            jumps += 1
    return jumps  

#06
# Complete the repeatedString function below.
def repeatedString(s, n):
    string = ""
    while len(string) < n:
        string += s

    string = string[:n]

    return string.count('a')
print(repeatedString("aba", 10))


#07
# Complete the simpleArraySum function below.
#
def simpleArraySum(ar):
    #
    # Write your code here.
    #
    if len(ar) > 1000:
        return False
    sum = 0

    for i in ar:
        sum += i
    return sum 

#08
# Complete the compareTriplets function below.
def compareTriplets(a, b):
    alice, bob = 0, 0

    for i in range(3): 
        if a[i] > b[i]: alice += 1
        if a[i] < b[i]: bob += 1
    
    return [alice, bob]

# Complete the aVeryBigSum function below.
def aVeryBigSum(ar):
    sum = 0
    for i in ar: sum += i
    return sum 

#09
#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

#10
def diagonalDifference(arr):
    # Write your code here
    
    primary, secondary = 0, 0
    for i in range(len(arr)):
        primary += arr[i][i] 
        secondary += arr[len(arr)-1-i][i]
    return abs(primary - secondary)


#11
# Complete the plusMinus function below.
def plusMinus(arr):

    positive, neutral, negative = 0, 0, 0
    num = len(arr)
    for i in arr: 
        if i > 0: positive += 1
        elif i < 0: negative += 1
        else: neutral += 1 
    print(positive/num)
    print(negative/num)
    print(neutral/num)
    """
#12
# Complete the staircase function below.
def staircase(n):
    string = ""
    for i in range(n):
        string += " "*(n-i-1) + "#"*(i+1)
        print (string)
        string = ""


#13
# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    sum, sum_arr = 0, []
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i != j: sum += arr[j]
        sum_arr.append(sum)
        sum = 0
    print(min(sum_arr), max(sum_arr))

#14
    
# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    tallest_candle_height = max(ar)
    total_tallest_candles = 0
    for candle_height in ar: 
        if candle_height == tallest_candle_height:
            total_tallest_candles += 1
    return total_tallest_candles
    

#15


#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #
    military_time = ''

    if s[-2] == 'A': #checks if AM or not
        if s[0:2] == '12': #checks if it's midnight hour
            military_time = '00' + s[2:-2] #converts midnight hour to '00' hr, deletes string 'PM'
        else:
            military_time = s[0:-2] #converts all other AM hrs to military 24 hour time format
    else:
        if s[0:2] != '12': #converts non-noon PM hrs to military 24 hr time format
            military_time = str((int(s[0:2]) + 12)%24) + s[2:-2] #deletes string 'PM'

        else:
            military_time = str(int(s[0:2])) + s[2:-2] #keeps noon hr as 12, deletes string 'PM'
    return military_time

#16

# Complete the queensAttack function below.
def queensAttack(n, k, r_q, c_q, obstacles):
    row_attacks, column_attacks, diagonal_attacks = 0, 0, 0 #possible of attacks
    #row attacks (columns left/right of queen)
    for i in range(1, n+1):
        
        for j in range(len(obstacles)):
            
            if i != c_q and obstacles[j][0] != r_q:            
            
                row_attacks += 1
                print(i, row_attacks)
    return row_attacks, column_attacks, diagonal_attacks
print(queensAttack(8, 2, 1, 3, [[2,2], [5,5]]))
                    
    

#17

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    final_grades, rounded_grade = [], 0
    for grade in grades:
    
        if grade < 38: #checks if grade is less than 38
            final_grades.append(grade)
        else:
            rounded_grade = round(grade/5)*5 #grade greater than 37 being rounded 
            if grade < rounded_grade and rounded_grade - grade < 3:
                final_grades.append(rounded_grade) #checks difference between grade and rounded_grade when rounded_grade is greater than grade
            elif grade > rounded_grade:
                final_grades.append(grade) #when grade is greater than rounded_grade
            else:
                final_grades.append(rounded_grade) #appends to final array
    return final_grades 
 
print(gradingStudents([73, 67, 38, 33]) == [75, 67, 40, 33]) #True
                    
#18

"""
Sam's house has an apple tree and an orange tree that yield an abundance of fruit. In the diagram below, the red region denotes his house, where  is the start point, and  is the endpoint. The apple tree is to the left of his house, and the orange tree is to its right. You can assume the trees are located on a single point, where the apple tree is at point , and the orange tree is at point .

Apple and orange(2).png

When a fruit falls from its tree, it lands  units of distance from its tree of origin along the -axis. A negative value of  means the fruit fell  units to the tree's left, and a positive value of  means it falls  units to the tree's right.

Given the value of  for  apples and  oranges, determine how many apples and oranges will fall on Sam's house (i.e., in the inclusive range )?

For example, Sam's house is between  and . The apple tree is located at  and the orange at . There are  apples and  oranges. Apples are thrown  units distance from , and  units distance. Adding each apple distance to the position of the tree, they land at . Oranges land at . One apple and two oranges land in the inclusive range  so we print

1
2
Function Description

Complete the countApplesAndOranges function in the editor below. It should print the number of apples and oranges that land on Sam's house, each on a separate line.

countApplesAndOranges has the following parameter(s):

s: integer, starting point of Sam's house location.
t: integer, ending location of Sam's house location.
a: integer, location of the Apple tree.
b: integer, location of the Orange tree.
apples: integer array, distances at which each apple falls from the tree.
oranges: integer array, distances at which each orange falls from the tree.
Input Format

The first line contains two space-separated integers denoting the respective values of  and .
The second line contains two space-separated integers denoting the respective values of  and .
The third line contains two space-separated integers denoting the respective values of  and .
The fourth line contains  space-separated integers denoting the respective distances that each apple falls from point .
The fifth line contains  space-separated integers denoting the respective distances that each orange falls from point .

Constraints

Output Format

Print two integers on two different lines:

The first integer: the number of apples that fall on Sam's house.
The second integer: the number of oranges that fall on Sam's house.
Sample Input 0

7 11
5 15
3 2
-2 2 1
5 -6
Sample Output 0

1
1
Explanation 0

The first apple falls at position .
The second apple falls at position .
The third apple falls at position .
The first orange falls at position .
The second orange falls at position .
Only one fruit (the second apple) falls within the region between  and , so we print  as our first line of output.
Only the second orange falls within the region between  and , so we print  as our second line of output.

"""

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    total_apples, total_oranges = 0, 0
    apples_at_distance = []
    oranges_at_distance = []

    for m in apples:
        apples_at_distance.append(m + a)
    for n in oranges:
        oranges_at_distance.append(n + b)

    for i in apples_at_distance:
        if i >= s and i <= t: total_apples += 1
    for j in oranges_at_distance:
        if j >= s and j <= t: total_oranges += 1
    print(total_apples)
    print(total_oranges)
        



#19

#20    



