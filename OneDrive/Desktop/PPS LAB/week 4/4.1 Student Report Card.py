n = int(input())

records = []
for _ in range(n):
    name, sub, marks = input().split()
    marks = int(marks)
    records.append((name, sub, marks))

students = tuple(sorted({record[0] for record in records}))

averages = []
for student in students:
    total = 0
    count = 0
    for record in records:
        if record[0] == student:
            total += record[2]
            count += 1
    avg = total / count
    averages.append((student, avg))

for student, avg in averages:
    print(f"{student} : {avg}")

topper_name, topper_avg = max(averages, key = lambda x : x[1])

print(f"Topper: {topper_name} with average {topper_avg}")
