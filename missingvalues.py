import os
import pandas as pd


data = {"Name": ["Liam", "diya", None, "Ava"], "Mark": [98, 94, None, 85]}
df = pd.DataFrame(data)


missing_summary = df.isnull().sum()
print("Missing values per column:")
print(missing_summary)


os.makedirs("missing_data", exist_ok=True)


missing_summary.to_csv("missing_data/summary.csv")
print("\nSaved summary to missing_data/summary.csv")