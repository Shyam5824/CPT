'''missing value operations on NAN'''
import pandas as pd 
import numpy as np
series=pd.Series([10,np.nan,30,np.nan,50],index=['a','b','c','d','e'])
print("\n Original series:")
print(series)

#check missing values
print("Missing values:")
print(series.isna())

#replace nan with 0
filled_series=series.fillna(0)
print("\n series after fillling NAN with 0:")
print(filled_series)

#missing values deletion 
dropped_series = series.dropna()
print("\n series after dropping missing values:")
print(dropped_series)