# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 16:31:07 2020

@author: Vladimir
"""


def laceStrings(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """
    
    result = ''
    x = len(s1)
    y = len(s2)
    
    while x != 0 and y != 0:
        result += s1[-x]
        x -= 1
        result += s2[-y]
        y -= 1
    
    if x != 0:
        result += s1[-x: ]
    if y != 0:
        result += s2[-y: ]
    
    return result     
    
    
    
if laceStrings('abcd', 'efghi') == 'aebfcgdhi':
    print ('success')
else:
    print ('not passed')
    
if laceStrings('abcd1234567', 'efghi') == 'aebfcgdh1i234567':
    print ('success')
else:
    print ('not passed')
    
if laceStrings('', 'efghi') == 'efghi':
    print ('success')
else:
    print ('not passed')
    
if laceStrings('abcd', '') == 'abcd':
    print ('success')
else:
    print ('not passed')
    
if laceStrings('a', 'efghi') == 'aefghi':
    print ('success')
else:
    print ('not passed')
    
    
if laceStrings('abcd', 'e') == 'aebcd':
    print ('success')
else:
    print ('not passed')
    
if laceStrings('', '') == '':
    print ('success')
else:
    print ('not passed')