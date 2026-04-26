
dictionary = {"numbers": [2, 3, 4, 5, 6, 7, 8, 9, 10]}


even_list = []
for num in dictionary["numbers"]:
    if num % 2 == 0:
        even_list.append(True)
    else:
        even_list.append(False)

dictionary["even"] = even_list

print("After adding 'even' key:")
print(dictionary)
print()


for i in range(len(dictionary["numbers"])):
    dictionary["numbers"][i] -= 1

print("After subtracting 1 from numbers:")
print(dictionary)
print()

last_value = dictionary["even"][-1]
dictionary["even"] = [last_value] + dictionary["even"][:-1]

print("After shifting the Boolean list:")
print(dictionary)
