'''num=int(input())
deno=int(input())
try:
    quo=num/deno
    print(quo)
except ZeroDivisionError:
    print("Deno cannot e zero")
    
    
try:
    num=int(input())
    print(num*4)
except KeyboardInterrupt:
    print("Number cannot be entered")
except ValueError:
    print("please enter the valid datatype")
print("Bye")

try:
    file=open("File.txt")
    str=file.readline()
    print(str)
    
except IOError:
    print("Error occured during input take")
else:
    print("Succefully ftched the data")
    
#raise [Exception [,args[,trackback]]]    
try:
    num=11
    print(num)
    raise ValueError
except:
    print("Exception occured")
    
    #Trackback(most recent calls)
    
    
try:
    print("Raising Exception")
    raise ValueError
except:
    print("Exception caught")
finally:
    print("Peforming the cleanup in finally")
    



c=int(input())
f=(c*9/5)+32
assert(f<=32), "Its Cold"
print("Fahrenheit:",f)


def display(n):
    while True:
        try:
            n+=1
            if n==21:
                raise StopIteration
        except StopIteration:
            break
        else:
            print(n,end=' ')
        
i=0
display(i)

import random
class RandomError(Exception):
    pass
try:
    num=random.random()
    if num<0.1:
        raise RandomError
except RandomError as e:
    print("Random error generated")
else:
    print("%.4f"%num)
    

from calendar import *
year=int(input("Enter a year number:"))
print(calendar(year,2,1,8,3))

from calendar import *
Year=int(input("Enter a year number:"))
Month=int(input("Enter a month number:"))
str=month(Year,Month)
print(str)

from calendar import *
year=int(input())
if isleap(year):
    print(year,'is leap year')
else:
    print(year,'is not a leap year')
    
#program to print the next 10 dates continously
from datetime import *
d=date.today()
print(d)
d=date(1996,6,29)
for x in range(1,10):
    nextdate=d+timedelta(days=x)
    print(nextdate)
    
    
import time
epoch=time.time()
print(epoch)
'''
#commnand line arg

import sys
if len(sys.argv)<2:
    print("Usage: python hi.py <name>")
else:
    name=sys.argv[1]
    print(f"student,{name}!")
    