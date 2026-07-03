num = int(input("enter first number :"))
n = int(input("enter the range :"))
print(f"multiplication table  of {num}")
for i in range(1,n+1):
    print(f"{num} x {i} = {i*num}")