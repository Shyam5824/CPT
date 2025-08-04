'''code to show the computation of statsitics and access series attributes 100 200 150 300 250
print original data,which is serialized 
stastics:
mean 
sum
max
min
Attributes:
index=['a'......'e']
values=[100.0..............250.0] '''


import pandas as pd
print("Enter 5 random numbers,space separated: ")
numbers=input().strip().split()
numbers=[float(num) for num in numbers]
try:
    if len(numbers)!=5:
        raise ValueError("Please enter 5 numbers only!!!")
    series=pd.Series(numbers,index=['a','b','c','d','e'])
    print("\n Orginal series:")
    print(series)
#Statistics
    print("\n Statstics:")
    print(f"Mean:{series.mean()}")
    print(f"sum:{series.sum()}")
    print(f"Max:{series.max()}")
    print(f"Min:{series.min()}")
#Attributes
    print("\n")
    print(f"Index:{series.mean()}")
    print(f"Values:{series.values.tolist()}")
    print(f"Datatype:{series.dtype}" 12 )
except ValueError as e:
    print(f"Error:{e}")


