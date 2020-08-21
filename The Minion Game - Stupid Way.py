#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 23:00:39 2020

@author: seangao
"""

def minion_game(string):
    vowels = ['A', 'E', 'I', 'O', 'U']
    consonants = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L',
     'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']

    string_lst = list(string)
    
    def removedup(input_list):
        lst = set()
        lst_add = lst.add
        return [x for x in input_list if not (x in lst or lst_add(x))]

    v_lst = [x for x in string_lst if x in vowels]
    v_lst = removedup(v_lst)

    c_lst = [x for x in string_lst if x in consonants]
    c_lst = removedup(c_lst)
    
    def getbases(letter):
        indices = [i for i,d in enumerate(string_lst) if d==letter]
        bases = []
        for i in indices:
            bases.append(string_lst[i:])
        return bases

    def substrgen(base):
        list_substr = []
        for i in range(1, len(base)+1):
            list_substr.append(base[:i])
        return list_substr
    
    def getsubstrs(letter):
        bases = getbases(letter)
        substrs = []
        for i in bases:
            substr = substrgen(i)
            substrs.append(substr)
            
        substrs = [item for sublist in substrs for item in sublist]
        return substrs
    
    def olcount(string, str_to_search_for):
        count = 0
        for x in range(len(string) - len(str_to_search_for) + 1):
            if string[x:x+len(str_to_search_for)] == str_to_search_for:
                count += 1
        return count
    
    def getpoints(letter):
        lst = getsubstrs(letter)
        lst = [''.join(x) for x in lst]
        lst = list(set(lst))
        lst = [olcount(string, x) for x in lst]
        return sum(lst)

    s = []
    for i in c_lst:
        output = getpoints(i)
        s.append(output)

    k = []
    for i in v_lst:
        output = getpoints(i)
        k.append(output)

    if sum(s) > sum(k):
        print('Stuart ' + str(sum(s)))
    elif sum(s) == sum(k):
        print('Draw')
    else:
        print('Kevin ' + str(sum(k)))