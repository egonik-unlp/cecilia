#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 08:40:38 2021

@author: gonik
"""

'''
Random Walks
'''


import matplotlib.pyplot as plt
import numpy as np

N = 100000

pasos = np.zeros(N)

for i in range(N):
    print(i)
    x = np.random.uniform(-1,1)
    pasos[i] = x 

acumulado = np.cumsum(pasos)


plt.plot(acumulado)

