import pandas as pd
n=int(input("Enter number of profiles:"))
names=[]
ages=[]
branches=[]
for i in range(n):
    print(f"----Enter {i+1}----")
    name=input("Enter name:")
    age=input("Enter Age:")
    branch=input("Enter Branch:")
    names.append(name)
    ages.append(age)
    branches.append(branch)
data={'Name':names,'Age':ages,'Branch':branches}
df=pd.DataFrame(data)
print("\nDataFrame created....")
print(df)