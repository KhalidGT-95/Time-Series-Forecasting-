# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 21:09:39 2017

@author: Khalid
"""

'''

Time Series Decomposition using Additive Decomposition Model

'''
import pandas as pd
from random import randrange
from pandas import Series
from matplotlib import pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
import numpy as np
#series = [i+randrange(10) for i in range(1,100)]

year1 = np.array([2.112,1.932,2.162,2.13,2.227,2.124,2.184,2.152,2.062,2.121,2.03,2.091])

year2 = np.array([2.109,1.996,2.173,2.163,2.233,2.142,2.182,2.129,2.138,2.215,2.156,2.212])

year3 = np.array([2.177,2.028,2.361,2.358,2.417,2.314,2.386,2.366,2.258,2.351,2.263,2.303])

year4 = np.array([2.341,2.081,2.344,2.314,2.432,2.317,2.309,2.271,2.185,2.363,2.283,2.38])

temp = np.concatenate((year1,year2),axis=0)

temp2 = np.concatenate((temp,year3),axis=0)

series = np.concatenate((temp2,year4),axis=0)

#==============================================================================
# print(series)
# 
# result = seasonal_decompose(series, model='additive',freq=2,two_sided=True,)
# 
# result.plot()
# result.show()
# 
#==============================================================================

# Function to calculate trend
def Trend(data):
    trend_vector = np.arange(48,dtype=float)
    
    window_size = 24
    subwindow_size = window_size/2
    for i in range(len(trend_vector)):
        prev_window = (i-12)
        if prev_window < 0:
            prev_window = 0
        
        after_window = (i + subwindow_size) 
        if after_window > 48:
            after_window = 48
        trend_vector[i] = float(series[prev_window:after_window].sum() ) / 24.0  
        
    return trend_vector

# Function to calculate seasonality
def Seasonality(data):
    seasonality_series = np.arange(12,dtype=float)
    for i in range(len(seasonality_series)):
        seasonality_series[i] = (data[i]+data[i+12]+data[i+24]+data[i+36]) / 4.0
    
    return seasonality_series

trends = Trend(series)

#==============================================================================
# print(len(trends))
# for i in range(len(trends)):
#     print(trends[i],end=' , ')
# print(trends[1:10])        
# 
# plt.plot(series)
# plt.plot(trends)
# plt.plot(seasonality_series)
# plt.plot(remainder_series)

# plt.show()        
#==============================================================================
## Now compute detrended series

detrended_series = np.arange(48,dtype=float)

for i in range(len(series)):
    detrended_series[i] = float(series[i] - trends[i])

seasons = Seasonality(detrended_series)

seasonality_series = np.tile(seasons,4)

remainder_series = detrended_series - seasonality_series  # To calculate the remainder
        
df = pd.DataFrame({'Time-Series':series,'Trend':trends,'Seasonality':seasonality_series,'remainder-Series':remainder_series})

df.plot()



