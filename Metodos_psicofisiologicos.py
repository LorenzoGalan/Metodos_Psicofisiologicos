# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 13:02:21 2021

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sy
from pprint import pprint

pupil= np.loadtxt("pupil_positions.csv", usecols= (6), delimiter=',', skiprows=1)
data = np.loadtxt('Flor.csv', usecols = (0),  delimiter=',')

pprint(data)

agregar_1= lambda x:x+10

list(map(agregar_1,pupil))

df=pd.DataFrame({"sujeto1":list(map(agregar_1,pupil))})
plt.plot(df)
df.to_csv("sujeto1.csv")
#%%
def agregar_1(numero):
    return numero + 10

agregar_1(1)
