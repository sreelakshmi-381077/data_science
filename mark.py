students = [
    {"name": "Liam", "mark": 98},
    {"name": "Sophia", "mark": 94},
    {"name": "Ethan", "mark": 89},
    {"name": "Ava", "mark": 85},
    {"name": "Noah", "mark": 81},
    {"name": "Jackson", "mark": 74},
    {"name": "Mia", "mark": 68},
    {"name": "Lucas", "mark": 61},
    {"name": "Isabella", "mark": 55},
    {"name": "Oliver", "mark": 52}
]


filtered_students = list(filter(lambda s: s["mark"] > 80, students))

sorted_students = sorted(filtered_students, key=lambda s: s["mark"], reverse=True)


print("Students with marks > 80 (Highest to Lowest):")
for student in sorted_students:
    print(f"{student['name']}: {student['mark']}")