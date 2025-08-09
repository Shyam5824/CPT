import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
hours=np.array([1,2,3,4,5]).reshape(-1,1)
marks=np.array([2,4,6,4,5])
model=LinearRegression()
model.fit(hours,marks)

new_hours=np.array([[6]])
prediction=model.predict(new_hours)
print(f"predicted marks for 6 hours:{prediction[0]:.2f}")

plt.scatter(hours,marks,color='blue',label="Original data")      
plt.plot(hours,model.predict(hours),color='red',label="Linear Regression")
plt.xlabel("Hours studied")
plt.ylabel(" Scored Marks")
plt.legend()
plt.show()




#realtimeMLR.py
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# age, milage, owners, engine cubic size
x = np.array([
    [3, 40, 1, 2.0],
    [5, 70, 2, 1.6],
    [1, 30, 2, 2.5],
    [8, 90, 3, 1.8],
    [8, 90, 3, 1.8],
    [6, 80, 2, 2.0],
    [2, 50, 1, 2.2],
    [4, 60, 1, 1.5],
    [7, 85, 3, 1.6]
])
y=np.array([20,15,25,10,14,12,22,18,11])

model = LinearRegression()
model.fit(x,y)
print("Intercept : ",model.intercept_)
print("Coefficients : ",model.coef_)
newcar=np.array([[4,55,2,1.8]])
predicted_price=model.predict(newcar)
print(f"Predicted Price for the car : ${predicted_price[0]*1000:.2f}")

y_pred=model.predict(x)
plt.scatter(y, y_pred, color='orange')
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'r--', lw=2)
plt.xlabel("Actual prize in $1000")
plt.ylabel("Predicted prize in $1000 ")
plt.title("Original vs predicted")
plt.show()


#numpyrand.py

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
np.random.seed(42)
x=np.random.rand(100)*10
#n=3x+5
y=3*x+5+np.random.randn(100)*2

m,c=np.polyfit(x,y,1)
print(f"Slope(m):{m:.2f}")
print(f"Intercept(c):{c:.2f}")

newx=7
print(f"Predicted y for x={newx}: {m*newx+c:.2f} ")

plt.scatter(x,y,color='blue',alpha=0.6,label='DataPoints')
plt.plot(x,m*x+c,color='red',lw=2,label='Best fitted line')
plt.xlabel('x-values')
plt.ylabel('y-values')
plt.legend()
plt.show()


#multipleLR.py

import numpy as np 
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

x=np.array([[5,2],
           [3,1],
           [8,3],
           [2,0],
           [6,2]])
y=np.array([72,50,90,30,85])


#train the model

model=LinearRegression()
model.fit(x,y)

print("Intercept:",model.intercept_)
print("Slope:",model.coef_)

y_pred=model.predict(x)

plt.scatter(y,y_pred,color='blue')
plt.plot([y.min(),y.max()],[y.min(),y.max()],'r--',lw=2)
plt.xlabel("Actual scores")
plt.ylabel("Predicted scores")
plt.title("Original vs Predicted")
plt.show()



#negative.py
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

np.random.seed(42)
x = np.random.rand(100, 1) * 10

y = -2 * x + np.random.normal(0, 1, (100, 1)) 

y = y.ravel()  # flatten y for sklearn

model = LinearRegression()
model.fit(x, y)

correlation = np.corrcoef(x.ravel(), y)[0, 1] 
print(f"Correlation coefficient: {correlation:.2f}")

plt.scatter(x, y, color='blue', label='Data Points')
plt.plot(x, model.predict(x), color='red', label='Regression Line')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Negative Correlation')
plt.legend()
plt.show()
