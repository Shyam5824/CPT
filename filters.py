"""code elobrates how to filter numerical data in series based on condition(eg:values greater than a threshold)"""

import pandas as pd 
print("Enter 4 random numbers , space separated:")
numbers = input().strip().split()
numbers = [float(num) for num in numbers]
try:
    if len(numbers) != 4:
        raise ValueError("Please provide exactly 4 numbers")
    total_data = pd.Series(numbers)
    print(total_data)

    filtered = total_data[total_data > 10]
    #0->5 1->15 2->8 3->18
    print("Values > 10:")
    print(filtered)
except ValueError as e:
    print(f"Error:{e}")
