# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 19:50:47 2020

@author: Vladimir
"""


def genPrimes():
    primeList = []
    nextPrime = 2

    while True:
        if nextPrime == 2:
            isPrime = True
        else:
            
            for prime in primeList:
                if (nextPrime%prime) != 0:
                    isPrime = True
                else:
                    isPrime = False
                    break

                
        if isPrime:
            primeList.append(nextPrime)
            next = nextPrime
            yield next
        nextPrime += 1
#better solution:
    
# =============================================================================
# def genPrimes():
#     primes = []   # primes generated so far
#     last = 1      # last number tried
#     while True:
#         last += 1
#         for p in primes:
#             if last % p == 0:
#                 break
#         else:
#             primes.append(last)
#             yield last
# =============================================================================
        
def genFib():
    fibn_1 = 1 #fib(n-1)
    fibn_2 = 0 #fib(n-2)
    while True:
        # fib(n) = fib(n-1) + fib(n-2)
        next = fibn_1 + fibn_2
        yield next
        fibn_2 = fibn_1
        fibn_1 = next