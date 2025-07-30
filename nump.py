'''numpy 
matrices - coordinates location
math functions statstics/ algebra



np.random.rand()
np.random.randn()
np.dot
np.arrange() random range of numbers
np.array() create/delete/access
np.zeros()/ones() creates an rentire array with 0/1
np.mean()
np.std()
np.unique()
np.linalg.inv()
'''
'''Arrays - import numpy'''

import numpy as np
'''x=np.array([1,2,3,4,5])
print("Array 1-D",x)


x=np.array([[1,2],[3,4]])
print("Array 2-D",x)

o=np.ones((3,6))
print("ones \n",o)

z=np.zeros((10,10))
print('zeros',z)


i=np.eye(8)
print("Identical coordinates:\n",i)

r=np.arange(0,11,2)
print("Array: ",r)

separate= np.linspace(0,1,5)
print("linspace",separate)

a=np.arange(1,10)
print(a)
reshaped=a.reshape((3,3))
print(reshaped)
linear=reshaped.reshape(-1)
print(linear)


a=np.arange(1,10)
print(a)
reshaped=a.reshape((3,3))
print(reshaped)
print("Element at (1,1):",reshaped[1,1])
linear=reshaped.flatten()
print(linear)
print("greater than 5:",linear[linear>5])
print("less than 5:",linear[linear<5])
print("Random numbers between 0 to 3:",np.random.rand(3))
print("random integer: \n",np.random.randint(1,100,(2,3)))


import numpy as np
matrix = np.full((3, 3), True, dtype=bool)
print(matrix)'''

matrix =np.zeros((3,3),dtype=bool)
print(matrix)