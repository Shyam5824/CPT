'''

import re functions

1.re.findall()
2.re.match()- 0-n-1(str1) 0-n-1(str2)
hello Hello
3.re.search()
4.re.sub()
5.re.compile()
6.re.split()
7.re.finditer()

cases in regex:
re.IGNORECASE/re.I
re.MULTILINE/re.M
re.DOTALL/re.D
re.VERBOSE/re.V

metachars-
^ -start of string
$ -end of string
* -occurences
+ -occurences
? -*+
[] -set of characters
() -grouping
\ -escape
. -newline
'''
'''
code to take a text data and fetch to match the given data
syntax: re.match(searched element,text)
import re
text='hi students how are you!!'
se=r'students'
output=re.match(se,text)
if output:
    print('Match found for:',output)
else:
    print('No match')

import re
text='hi students how are you!!'
se=r'hi'
output=re.match(se,text)
if output:
    print('Match found for:',output.group())
else:
    print('No match..')


import re
text='My number is 229'
match=re.search(r'\d+',text)
print(match)
print(group.match())

import re
text=input("Enter a sentence with a number")
match=re.search(r'\d+',text)
if match:
    print("number found ",match.group())
else:
    print("No match")

import re
text=input("Enter a sentence with a number")
match=list(re.finditer(r'\d+',text))
if len(match)>=2:
    print("Second number found ",match[1].group())
elif len(matches)==1:
    print("Only one number found",match[0].group())
else:
    print("No match")



import re
text=input("Enter a sentence with a number")
n=int(input("Which number you want to extract:"))
matches=re.findall(r'/d+',text)
if len(matches)>=n:
    print(f"{n}th number is:",matches[n-1])
else:
    print("Not found")
    



import re
email=input("Enter the email")
pattern=r'^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.[a-zA-Z]{2,}$'
if re.match(pattern,email):
    print("Valid")
else:
    print("Not valid")


'''



import re
phone=input("Enter the phone number")
pattern=r'^[6-9]\d{9}$'
if re.match(pattern,phone):
    print("Valid")
else:
    print("Not valid")
