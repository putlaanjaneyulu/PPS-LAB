
a = set(input("Enter students in Course A: ").split())
b = set(input("Enter students in Course B: ").split())
c = set(input("Enter students in Course C: ").split())

all_three = a & b & c


exactly_two = (a & b - c) | (b & c - a) | (a & c - b)

only_one = (a - b - c) | (b - a - c) | (c - a - b)

print("Students enrolled in all three courses:", all_three)
print("Students enrolled in exactly two courses:", exactly_two)
print("Students enrolled in only one course:", only_one)
