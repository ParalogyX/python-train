# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 18:33:04 2020

@author: Vladimir
"""
import random

def evalQuadratic(a, b, c, x):
   '''
   a, b, c: numerical values for the coefficients of a quadratic equation
   x: numerical value at which to evaluate the quadratic.
   '''
   return a*x*x + b*x + c


def twoQuadratics(a1, b1, c1, x1, a2, b2, c2, x2):
    '''
    a1, b1, c1: one set of coefficients of a quadratic equation
    a2, b2, c2: another set of coefficients of a quadratic equation
    x1, x2: values at which to evaluate the quadratics
    '''
    print (evalQuadratic(a1, b1, c1, x1) + evalQuadratic(a2, b2, c2, x2))
    return evalQuadratic(a1, b1, c1, x1) + evalQuadratic(a2, b2, c2, x2)


def twoQuadraticsTest():
    correct = True
    
    for i in range(1,50):
        a1 = random.randint(-1000, 1000)
        b1 = random.randint(-1000, 1000)
        c1 = random.randint(-1000, 1000)
        x1 = random.randint(-1000, 1000)
        
        a2 = random.randint(-1000, 1000)
        b2 = random.randint(-1000, 1000)
        c2 = random.randint(-1000, 1000)
        x2 = random.randint(-1000, 1000)
        
    
        if (a1*x1*x1 + b1*x1 + c1 + a2*x2*x2 + b2*x2 + c2) != twoQuadratics(a1, b1, c1, x1, a2, b2, c2, x2):
            correct = False
            break
    
    return correct