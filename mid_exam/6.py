# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 18:10:00 2020

@author: Vladimir
"""


a = [1,2,3]
print ('var a, type ' + str(type(a)) + ' , value ' + str(a))
b = (1,2,3)
print ('var b, type ' + str(type(b)) + ' , value ' + str(b))
c = ([1,2,3],['a','b','c'],[123])
print ('var c, type ' + str(type(c)) + ' , value ' + str(c))
d= c[0]
print ('var d, type ' + str(type(d)) + ' , value ' + str(d))