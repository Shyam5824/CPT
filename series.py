'''import pandas as pd
 
1. series (1-D Array)
2. Dataframes (2-D Array)/ labeling will be on rows and column
operations:
1. reading / writing of data (csv/json/xls)
2. inserting of data
3. selecting of data
4. data manipulation
5. grouping and aggregation
5. merging / joining
7. sorting
 
'''

import pandas as pd
print("Enter 3 names seperated with space:")
names = input().strip().split()
print("Enter 3 index labels:")
indices = input().strip().split()
try:
    if len(names)!=3 or len(indices)!=3:
        raise ValueError("Please provide exact names with indices")
    series=pd.Series(data=names,index=indices)
    print("Created a new series: ")
    print(series)
except ValueError as e:
    print(f"Error:{e}")