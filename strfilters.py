'''code elobrates how to filter string data in series based on insensitivity'''

import pandas as pd
print("Enter 5 strings ,space separated: ")
strings=input().strip().split()
print("Enter substring:")
substring=input().strip()
try:
    if len(strings)!=5:
        raise ValueError("Please provide 5 strings only:")
    series=pd.Series(strings)
    print("Original series:")
    print(series)
    filtered_series=series[series.str.lower().str.contains(substring.lower(),na=False)]
    print(f"strings containing '{substring}'(case-insensitive):")
    print(filtered_series if not filtered_series.empty else "No match found .")
except ValueError as e:
    print(f"Error:{e}")
