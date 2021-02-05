#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 08:17:05 2021

@author: gonik
"""

import numpy as np
import matplotlib.pyplot as plt


N = 100000
nr = 0

xin = []
yin = []
xout = []
yout = []



for i in range(N):
    x = np.random.random()
    y = np.random.random()
    r = np.sqrt(x**2 + y**2)
    if r < 1:
        xin.append(x)
        yin.append(y)
        nr = nr + 1
    else:
        xout.append(x)
        yout.append(y)
        
        
print((nr/N)*4)


plt.scatter(xin,yin, c = 'r', label = 'in')
plt.scatter(xout, yout, c= 'g', label = 'out')
#plt.legend()
plt.show()