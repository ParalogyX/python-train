# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 18:04:40 2020

@author: Vladimir
"""


def f(x):
    a = []
    while x > 0:
        a.append(x)
        f(x-1)
        
f(3)        