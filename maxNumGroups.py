#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 17:43:43 2019

@author: bijayamanandhar
"""

def maximumGroups(complianceFactors):
    # Write your code here

    maxNumOfGroups = 0

    tempList = []
    for i in range(len(complianceFactors) - 1):

        tempTotal = 0


        if complianceFactors[i] not in tempList:

            tempList.append(complianceFactors[i])

            tempTotal += 1

            listToCount = complianceFactors[i+1:]

            for j in range(len(listToCount)):

                if listToCount[j] == complianceFactors[i]:

                    tempTotal += 1

            maxNumOfGroups += tempTotal // 2

    return maxNumOfGroups

print(maximumGroups([4,5,2,2,4,4,3,3]))


