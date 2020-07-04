# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 18:26:10 2020

@author: Vladimir
"""




def Square(x):
    return SquareHelper(abs(x), abs(x))

def SquareHelper(n, x):
    if n == 0:
        return 0
    return SquareHelper(n-1, x) + x