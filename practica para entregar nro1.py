# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 23:02:45 2021

@author: Gigabyte
"""

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(r"C:\Users\Gigabyte\Desktop\cecilia-main\datos\country_vaccinations.csv" , encoding="utf-8")
#print(df)
#print(df.columns)                   

#Voy a realizar un grafico en barras de personas vacunadas vs vacunas

#print(df[['people_vaccinated','vaccines']])   #tome las dos columnas de interes

vacunados=df[['people_vaccinated','vaccines']]


#print(vacunados)

x=df['vaccines']
y=df['people_vaccinated']
print(plt.bar(x,y))