# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 19:59:16 2020

@author: Vladimir
"""


def general_poly (L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
    def poly(x):
        kMax = len(L)-1
        result = 0
        for k in range (0, kMax+1):
            result += L[k] * x**(kMax-k)
        return result
    
    return poly


def general_poly_test():
    foo = general_poly ([1,2,3,0.123,1024212,-15,0.1,12312.99,12.5,-12.5,0,0,99,-12312389])
    
    
    print( foo (2))
    print(foo(10))
    print(foo(-10))
    print(foo(0)) 
    print(foo(-19))
    print(foo(0.5))        
        
general_poly_test()