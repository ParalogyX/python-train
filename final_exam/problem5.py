# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 17:11:12 2020

@author: Vladimir
"""


def uniqueValues(aDict):
    '''
    aDict: a dictionary
    returns: a sorted list of keys that map to unique aDict values, empty list if none
    '''
    
    result = []

    
    for index1 in aDict.keys():
        isUniq = True
        i = 0
        for index2 in aDict.keys():
            if aDict[index1]== aDict[index2]:
                i += 1
            if i > 1:
                isUniq = False
                
                
        if isUniq:
            result.append(index1)
    
    
    result.sort()
    
    return result


aDict = {1: 1, 3: 2, 6: 0, 7: 0, 8: 4, 10: 0}
aDict = {1: 1, 2: 1, 3: 1}
aDict = {23:98, 12:13, 14:27, 9:12, 56: 99}


print(uniqueValues(aDict))