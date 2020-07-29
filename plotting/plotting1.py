# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 21:45:28 2020

@author: vpe
"""


import pylab as plt
import math

mySamples = []
myLinear = []
mySquare = []
myCubic = []
myExp = []
myLog = []

for i in range (0, 30):
    mySamples.append(i)
    myLinear.append(i)
    mySquare.append(i**2)
    myCubic.append(i**3)
    myExp.append(1.5**i)
    if (i != 0):
        myLog.append(math.log(i,2))
    else:
        myLog.append(0)
    
plt.figure('Log')
plt.clf()
plt.title('Logarifmic')
plt.xlabel('Samples')
plt.ylabel('Log2')
plt.plot (mySamples, myLog)   
plt.figure('Lin')
plt.clf()
plt.title('Linear')
plt.xlabel('Samples')
plt.ylabel('Lin')
plt.plot (mySamples, myLinear)
plt.figure('Square')
plt.clf()
plt.title('Square')
plt.xlabel('Samples')
plt.ylabel('Square') 
plt.plot (mySamples, mySquare)
plt.figure('cubic') 
plt.clf()
plt.title('Cubic')
plt.xlabel('Samples')
plt.ylabel('Cubic')
plt.plot (mySamples, myCubic)
plt.figure('Exp')
plt.clf()
plt.title('Exponantial')
plt.xlabel('Samples')
plt.ylabel('Exp') 
plt.plot (mySamples, myExp)