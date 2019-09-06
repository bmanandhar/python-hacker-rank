#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 11:42:34 2019

@author: bijayamanandhar
"""

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
            elif grade > rounded_grade and grade - rounded_grade < 3:
                final_grades.append(grade) #checks difference between grade and rounded_grade when grade is greater than rounded_grade
            else:
                final_grades.append(rounded_grade) #appends to final array
    return final_grades 
 
print(gradingStudents([73, 67, 38, 33]) == [75, 67, 40, 33]) #True