import pandas as pd


data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Emma"],
    "Age": [20, 21, 19, 22, 20],
    "Marks": [85, 90, 88, 92, 87]
}


df = pd.DataFrame(data)


df.to_csv("students.csv", index=False)


df = pd.read_csv("students.csv")


print("First Row:")
print(df.head(1))


print("\nLast Row:")
print(df.tail(1))