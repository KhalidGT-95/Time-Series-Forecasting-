# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 17:34:01 2017

@author: Khalid
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

months = np.array([1,2,3,4,5,6,7,8,9,10,11,12])

year1 = np.array([2.112,1.932,2.162,2.13,2.227,2.124,2.184,2.152,2.062,2.121,2.03,2.091])

year2 = np.array([2.109,1.996,2.173,2.163,2.233,2.142,2.182,2.129,2.138,2.215,2.156,2.212])

year3 = np.array([2.177,2.028,2.361,2.358,2.417,2.314,2.386,2.366,2.258,2.351,2.263,2.303])

year4 = np.array([2.341,2.081,2.344,2.314,2.432,2.317,2.309,2.271,2.185,2.363,2.283,2.38])

obj1 = pd.Series(year1,index=['year1' for x in range(12)])
obj2 = pd.Series(year2,index=['year2' for x in range(12)])
obj3 = pd.Series(year3,index=['year3' for x in range(12)])
obj4 = pd.Series(year4,index=['year4' for x in range(12)])

data_range = pd.date_range(start='1998',end='12/1/2001',freq='MS')

print(len(data_range))

oo = obj1.append(obj2).append(obj3).append(obj4)


df = pd.DataFrame({'Monthly value':oo})


diagram = df.plot(title='Yearly values graph plot')
diagram.set_xlabel('Years')
diagram.set_ylabel('Values')

index_array = oo.index
values = oo.values
