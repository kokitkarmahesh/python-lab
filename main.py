
import pandas as pd
import numpy as np

# Step 1: Read Excel file
df = pd.read_excel("sample_data.xlsx")

# Step 2: Display Excel data
print("Excel Data:")
print(df.to_string(index=False))

# Step 3: Convert to NumPy array
data = df.to_numpy()

# Step 4: Display NumPy array
print("\nNumPy Array:")
print(data)

# Step 5: Display array information
print("\nArray Shape:", data.shape)
print("Number of Rows:", data.shape[0])
print("Number of Columns:", data.shape[1])
