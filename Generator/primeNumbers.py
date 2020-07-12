# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 19:50:47 2020

@author: Vladimir
"""


def genPrimes():
    prime_1 = 2
    prime_2 = 3
    while True:
        if (prime_2%prime_1) != 0:
            #to keep a list?
            print("prime_1 = " + str (prime_1))
            print("prime_2 = " + str (prime_2))
            next = prime_2
            yield next
            prime_1 = prime_2
            prime_2 = next
            
        else:
            prime_2 += 1
            print("not prime: " + str(prime_2))
        
        
def genFib():
    fibn_1 = 1 #fib(n-1)
    fibn_2 = 0 #fib(n-2)
    while True:
        # fib(n) = fib(n-1) + fib(n-2)
        next = fibn_1 + fibn_2
        yield next
        fibn_2 = fibn_1
        fibn_1 = next