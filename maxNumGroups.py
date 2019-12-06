#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 17:43:43 2019

@author: bijayamanandhar
"""

def maximumGroups(complianceFactors):
    # Write your code here
    # max number of groups, initial value zero
    maxNumOfGroups = 0
    # checking if the element has been already been counted
    tempList = []
    # iterates all elements except the last
    for i in range(len(complianceFactors) - 1):
        # counter for each element
        tempTotal = 0
        # if the element has not already been counted
        if complianceFactors[i] not in tempList:
            # keeps all elements for ref once counted
            tempList.append(complianceFactors[i])
            # adds 1 to counter if present
            tempTotal += 1
            # generates another list for couting the element considered
            listToCount = complianceFactors[i+1:]
            # checking the new list if the element is present
            for j in range(len(listToCount)):
                # when considered element is found
                if listToCount[j] == complianceFactors[i]:
                    # adds 1 to counter
                    tempTotal += 1
            # adds the num of groups at the end
            maxNumOfGroups += tempTotal // 2

    return maxNumOfGroups

print(maximumGroups([4,5,2,2,4,4,3,3]) == 3) # True


