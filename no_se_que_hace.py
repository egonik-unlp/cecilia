#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Fri Aug 20 19:02:40 2021

@author: victoria
"""

# Método de Monte Carlo para calcular pi



import numpy as np
import matplotlib.pyplot as plt



def no_se_que_hace(N):
    nr=0
    xin=[]
    xout=[]
    yin=[]
    yout=[]
    for i in range(N):
        x=np.random.random() #0 y 1 con distribucion uniforme 
        y=np.random.random() #0 y 1 con distribucion uniforme 
        r=np.sqrt(x**2 + y**2)
        if r < 1:
            xin.append(x)
            yin.append(y)
            nr+=1
        else:
            xout.append(x)
            yout.append(y)
            
    return xin, yin, xout, yout
    #return (nr/N)*4


xin,yin,xout,yout=no_se_que_hace(100000)


plt.scatter(xin,yin, c="green", s=.1,label="in")
plt.scatter(xout, yout, c="red", s=.1,label="out")
plt.legend()
plt.savefig("monte_carlo.png")
plt.show()


