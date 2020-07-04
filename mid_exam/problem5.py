# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 19:08:11 2020

@author: Vladimir
"""


def keysWithValue(aDict, target):
    '''
    aDict: a dictionary
    target: an integer
    '''
    
    keyList = []
    
    for key in aDict.keys():
        if (aDict[key] == target):
            keyList.append(key)
            
    keyList.sort()
    
    return keyList
            