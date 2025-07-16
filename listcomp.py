'''r=[int(x) for x in input().split()[:5]]
print(r)

colors=['red','green','blue','violet']
print([color.upper() for color in colors])


print([x for x in range(11) if x%2==0])

m=[[1,2,3],[4,5,[11,22]],[6,7,8]]
print(m[1][2][0])


user_input = input("Enter 9 space-separated numbers: ")
numbers = [int(num) for num in user_input.split()]

if len(numbers) != 9:
    print("Please enter exactly 9 numbers.")
else:
    matrix = [numbers[i:i+3] for i in range(0, 9, 3)]
    for row in matrix:
        print(row)


nums=[int(x) for x in input().split()[:9]]
m=[[nums[i*3+j] for j in range(3)] for i in range(3)]
print("3X3 matrix")
for x in m:
    print(x)


nums=[int(x) for x in input().split()[:9]]
m=[[nums[i*3+j] for j in range(3)] for i in range(3)]
if m[i][j]%2==0:
    print(1)
else:
    print(0)
print(m)


nums=input().split()
numbers=[int(x) for x in nums]
m=[[numbers[i*3+j] for j in range(3)] for i in range(3)]
bm=[[0 if m[i][j]%2==0 else 1 for j in range(3)] for i in range(3)]
for r in m:
    print(r)
for r in bm:
    print(r)



nums_input = input("Enter exactly 9 numbers separated by spaces: ")
nums = nums_input.split()

if len(nums) != 9:
    print("Error: Please enter exactly 9 numbers.")
else:
    # Convert all input strings to integers
    numbers = [int(x) for x in nums]

    # Create the 3x3 matrix 'm'
    m = []
    for i in range(3):
        row = []
        for j in range(3):
            row.append(numbers[i * 3 + j])
        m.append(row)

    # Create the binary matrix 'bm'
    bm = []
    for i in range(3):
        row = []
        for j in range(3):
            if m[i][j] % 2 == 0:
                row.append(0)  # Even
            else:
                row.append(1)  # Odd
        bm.append(row)

    print("\nOriginal Matrix (m):")
    for r in m:
        print(r)

    print("\nBinary Matrix (bm):")
    for r in bm:
        print(r)




n=5

for i in range(n):
    for j in range(n):
        if i==0 or i==n-1:
            print("*",end=' ')
        elif j==0 or j==n-1:
            print("*",end=' ')
        elif i==j or i==n-i-1:
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()
'''

n=9
p=[' '.join(" " if(abs(i-n//2)+abs(j-n//2)<n//2) and i!=0 and i!=n-1 else "*" for j in range(n)) for i in range(n)]
for r in p:
    print(r)



 
