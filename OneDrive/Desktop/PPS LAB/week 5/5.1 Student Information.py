student = {
    "Firstname": "Rahul",
    "Lastname": "Sharma",
    "Sex": "Male",
    "Age": 21,
    "Course": "Literature",
    "Hobby": "Swimming"
}

print("a. Keys and Values:")
for key, value in student.items():
    print(f"{key} : {value}")

print("b. Keys:", student.keys())

print("c. Values:", student.values())

student["Course"] = "Foreign Languages"
print("d. After updating course:", student)

student["Address"] = "New York"                 
student.update({"Phone number": "9876543210"})  
print("e. After adding Address and Phone number:")
print(student)

student.pop("Sex")
student.pop("Hobby")
print("f. After removing Sex and Hobby:")
print(student)
