import numpy as np 
import pickle 
data=np.array([[1,2,3],[4,5,6]])

with open('data.pkl','wb') as file:
    pickle.dump(data,file)

with open('data.pkl','rb') as file:
    loaded_data=pickle.load(file)
print(loaded_data)


#multi.py
import pickle

my_list=[10,2,3,'Vijay',True]
with open('list.pkl','wb') as f:
    pickle.dump(my_list,f)
with open('list.pkl','rb') as f:
    loaded_list=pickle.load(f)
print(loaded_list)

#pickclass.py
import pickle
class Student:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def hi(self):
        return f"Hello, my name is {self.name}."
s=Student('Vijay',34)

with open('student.pkl','wb') as f:
    pickle.dump(s,f)
with open('student.pkl','rb') as f:
    loadeddata=pickle.load(f)
print(loadeddata.name)
print(loadeddata.hi())

 #plotpickle.py
 import matplotlib.pyplot as plt 
import pickle

fig, ax=plt.subplots()
ax.plot([1,2,3,4],[11,22,33,44],label="Line")       
ax.set_title("Sample plot")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.legend()

with open('plot.pkl','wb') as f:
    pickle.dump(fig,f)
plt.close(fig)
    
with open('plot.pkl','rb')as f:
    loadedfig=pickle.load(f)
    
#loadedfig.show()
plt.show(block=True)

#pears.py

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

np.random.seed(42)
theta=np.linspace(0,6*np.pi,500)
r=np.linspace(0,50,500)
np.random.normal(0,2,500)
x=r*np.cos(theta)
y=r*np.sin(theta)

r_value,p_value=pearsonr(x,y)

plt.figure(figsize=(7,7))
plt.scatter(x,y,c=theta,cmap='plasma',s=5,alpha=0.8)
plt.title(f"Pearson plot r={r_value:3f}",fontsize=15)
plt.colorbar(label="Angle theta")
plt.show()

#3d in above remove z
#Same above code in 3D
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
from mpl_toolkits.mplot3d import Axes3D 
np.random.seed(42)
theta=np.linspace(0,6*np.pi,800)
r=np.linspace(0,50,800) +np.random.normal(0,2,800)
z=np.linspace(-10,10,800)
x=r*np.cos(theta)
y=r*np.sin(theta)

r_value,p_value=pearsonr(x,y)
fig= plt.figure(figsize=(8,8))
ax= fig.add_subplot(111, projection='3d')
sc=ax.scatter(x,y,z,c=theta,cmap='plasma',s=5,alpha=0.8)
plt.title(f"Pearson plot r={r_value:.3f}",fontsize=15)
plt.colorbar(sc,ax=ax,label="Angle theta")
plt.show()