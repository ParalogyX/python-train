# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 16:56:47 2020

@author: Vladimir
"""


def primes_list_amount(N):
    '''
    N: an integer
    Returns a list of prime numbers
    '''
    
    result = [2]
    i = 2
    while N > 0:
        isPrime = True
        for k in result:
            if i % k == 0:
                isPrime = False
                break
        if isPrime:
            result.append(i)
            N -= 1
        i += 1
        
    return result


def primes_list(N):
    '''
    N: an integer
    Returns a list of prime numbers
    '''
    result = [2]
    i = 2
    while i <= N:
        isPrime = True
        for k in result:
            if i % k == 0:
                isPrime = False
                break
        if isPrime:
            result.append(i)
        i += 1
        
    return result



#print (primes_list_amount(100))
print (primes_list(0))