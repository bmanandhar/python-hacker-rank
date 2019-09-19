#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 20:58:17 2019

@author: bijayamanandhar
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 09:39:19 2019

@author: bijayamanandhar
"""  

#Vanity Phone Numbers
"""
Given:
A list(array) of vanity code in alpha characters.
A list of telephone numbers.
Form a list(array) of phone numbers selected to match vanity codes.
Key-pad has alpha characters as:
    2=ABC, 3=DEF, 4=GHI, 5=JKL, 6=MNO, 7=PQRS, 8=TUV, 9=WXYZ.

"""

def match_vanity_phone(codes, numbers):
    
    #dictionary of alpha-chars corresponding to key-numbers
    code_dic = {'2':'ABC', '3':'DEF', '4':'GHI', '5':'JKL', 
           '6':'MNO', '7':'PQRS', '8':'TUV', '9':'WXYZ'}
    
    #array to collect number converted from code
    code_to_num_arr = []
    
    #array to collect selected phone-nos    
    selected_phones = []
    
    #string to form code-converted number
    temp = ''
    
    #iterates thru array of codes
    for code in codes:
        
        #checking each chars to convert to number
        for i in range(len(code)):
            
            #tracks corresponding number matched with alpha-character
            for key in code_dic:
                
                #matching each character to get corresponding number
                if code[i] in code_dic[key]:
                    
                    #forming corresponding number to match alpha-code
                    temp += key
                    
        #forming array of code-converted numbers
        code_to_num_arr.append(temp)
        
        #after each alpha-code in the array, temp is made empty
        temp = ''
        
    #search for matching number to select 
    for num in code_to_num_arr:
        
        #iterates array of telephone numbers in search of corresponding alpha codes
        for number in numbers:
    
            #checks if the alpha code is present as the last string in the number            
            if num == number[-len(num):]:
                
                #if found, adds to the array
                selected_phones.append(number)

    return selected_phones


#Test case:
    
alpha_codes = ['TWILIO', 'HELLO', 'ENGLAND', 'JAPAN', 'ITALY', 'FRANCE']

telephone_numbers = ['+1415996643556', '+291348877773238', 
                     '+38461324372623', '+46457127848259', 
                     '+56536894546', '+63945129952726',
                     '+77377634254777991', '+8401892383645263']

expected = ['+56536894546', '+1415996643556',
            '+8401892383645263', '+63945129952726',
            '+46457127848259', '+38461324372623']
print(match_vanity_phone(alpha_codes, telephone_numbers) == expected) #True




