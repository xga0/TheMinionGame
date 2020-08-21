#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 23:00:39 2020

@author: seangao
"""

def minion_game(string):
    vowels = 'AEIOU'
    
    kevsc = 0
    stusc = 0
    for i in range(len(string)):
        if string[i] in vowels:
            kevsc += (len(string)-i)
        else:
            stusc += (len(string)-i)
            
    if kevsc > stusc:
        print('Kevin', kevsc)
    elif kevsc < stusc:
        print('Stuart', stusc)
    else:
        print('Draw')
        
minion_game('BABAA')