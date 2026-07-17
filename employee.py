import os
import pandas as pd


data = {
    'Department': ['HR', 'Engineering', 'Marketing', 'Engineering', 'HR', 'Marketing', 'Engineering'],
    'Salary': [60000, 95000, 70000, 110000, 65000, 72000, 105000]
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
print("-" * 40)


avg_salary_df = df.groupby('Department')['Salary'].mean().reset_index()
avg_salary_df.rename(columns={'Salary': 'Average_Salary'}, inplace=True)
print("Average Salary by Department:")
print(avg_salary_df)
print("-" * 40)


directory_name = "employee_reports"
os.makedirs(directory_name, exist_ok=True)
print(f"Directory '{directory_name}' is ready.")


output_path = os.path.join(directory_name, "average_salaries.csv")
avg_salary_df.to_csv(output_path, index=False)
print(f"Results successfully saved to: {output_path}")