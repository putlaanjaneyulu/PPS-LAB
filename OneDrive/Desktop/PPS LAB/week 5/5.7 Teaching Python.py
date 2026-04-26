students = {}

students["Basic"] = ["Anil", "Meena"]
students["Advanced"] = ["Ravi", "Sneha", "Kiran"]


students["Basic"].append("Sita")

students["Basic"] += ["Aman"]

students["Basic"].extend(["Neha"])

students["Advanced"].insert(0, "Rahul")


students["Basic"].remove("Meena")
students["Advanced"].append("Meena")

print("Students Dictionary:")
print(students)
print()

print("--- Printing items using .items() ---")
for course, student_list in students.items():
    print("Course:", course, "-> Students:", student_list)
print()



print("--- Printing items using dictionary keys ---")
for course in students:
    print("Course:", course, "-> Students:", students[course])

print()

print("Only course names:")
for course in students.keys():
    print(course)
print()

print("Only student lists:")
for student_list in students.values():
    print(student_list)
