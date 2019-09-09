#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 20:12:06 2019

@author: bijayamanandhar
"""

#Prefix phone

"""
Given:
    
-A list of prefixes for discount on phone calls
-A list of phone numbers
-Select the prefix phones and form a list as result     
"""

#prefixes and numbers both are lists(array)
def prefix_phone(prefixes, numbers):

    #empty array for result    
    selected = []
    
    #iterates thru prefix list
    for prefix in prefixes:

        #checks number to match prefix
        for number in numbers:
            
            #search for prefix in number
            if prefix == number[0:len(prefix)]:
                
                #adds number to array if matches
                selected.append(number)
    
    return selected
    
prefixes = ['+1234', '+5678', '+3215', '+987' ]

numbers = ['+9872349871', '+9871234665432', '+8712345671', 
           '+32159865342', '45452677721', '+5678111222333', 
           '+8362412300', '+82726241611']    

expected = ['+5678111222333', '+32159865342', 
            '+9872349871', '+9871234665432']

print(prefix_phone(prefixes, numbers) == expected) # True



#End of file