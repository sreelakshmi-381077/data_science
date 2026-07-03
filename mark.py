
def total_marks(m1, m2, m3):
    return m1 + m2 + m3


def percentage(total):
    return total / 3

def grade(per):
    if per >= 90:
        return "A+"
    elif per >= 80:
        return "A"
    elif per >= 70:
        return "B"
    elif per >= 60:
        return "C"
    elif per >= 50:
        return "D"
    else:
        return "Fail"

m1 = float(input("Enter Mark 1: "))
m2 = float(input("Enter Mark 2: "))
m3 = float(input("Enter Mark 3: "))

total = total_marks(m1, m2, m3)
per = percentage(total)
g = grade(per)

print("\nTotal Marks =", total)
print("Percentage =", per)
print("Grade =", g)
student = ( "" )
print("\nTotal Marks =", total)