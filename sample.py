'''import sys
print("Script name:",sys.argv[0])
print("All args:",sys.argv[1:])
print("Number of items:",len(sys.argv))
print("Including file name:",sys.argv)
if len(sys.argv)>1:
    print("First arg:",sys.argv[1])
else:
    print("No arguments provided")

import sys
num1=int(sys.argv[1])
num2=int(sys.argv[2])
num3=int(sys.argv[3])
print("product:",num1*num2*num3)


import sys
if len(sys.argv)!=3:
    print("Usage : python sample.py l b")
else:
    l=float(sys.argv[1])
    b=float(sys.argv[2])
    print("Calculated area:", l*b)
    

import sys
if len(sys.argv)<2:
    print("Usage: python sample.py n1,n2,.. n")
    sys.exit()
numbers=[int(argv) for arg in sys.argv[1:]]
total=sum(numbers)
print("Numbers:",numbers)
print("Sum:",total)


import argparse
parser= argparse.ArgumentParser(description=" Add 2 Numbers")
parser.add_argument('--x',type=int,required=True,help="first number")
parser.add_argument('--y',type=int,required=True,help="second number")
args=parser.parse_args()
result=args.x+args.y
print("Sum is:",result)

import argparse
parser= argparse.ArgumentParser(description=" Simple calculator")
parser.add_argument('--x',type=int,required=True,help="first number")
parser.add_argument('--y',type=int,required=True,help="second number")
parser.add_argument('--opt',type=str,required=True, choices=['add','sub','mul','div'],help="operation")
args=parser.parse_args()
if args.opt=='add':
    result=args.x+args.y
elif args.opt=='sub':
    result=args.x-args.y
elif args.opt=='mul':
    result=args.x*args.y
elif args.opt=='div':
    result=args.x/args.y
print("Result is:",result)

import os
path='.'
files=os.listdir(path)
print("Files and folders in current directory:")
for f in files:
    print(f)


import os
folder="new_folder"
if not os.path.exists(folder):
    os.mkdir(folder)
    print(f"Folder '{folder}' created")
else:
    print(f"Folder '{folder}' already exists")




import os
file="deleteme.txt"
if os.path.exists(file):
    os.remove(file)
    print(f"{file} deleted")
else:
    print("File not found")
'''


import os
file='shift.py'
if os.path.exists(file):
    size=os.path.getsize(file)
    print(f"{file} size:{size} bytes.")
else:
    print("File not found")
    
