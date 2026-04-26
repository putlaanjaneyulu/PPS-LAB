
pets = [
    {"name": "Toby", "animal type": "dog", "age": 2},
    {"name": "Kitty", "animal type": "cat", "age": 5},
    {"name": "Tiki", "animal type": "parrot", "age": 1}
]

new_pet = {"name": "Sugar", "animal type": "horse", "age": 4}
pets.append(new_pet)
print("After adding new patient:")

for pet in pets:
    print(pet)

print("\nAnimal names (using elements):")
for pet in pets:
    print(pet["name"])

print("\nAnimal names (using indices):")
for i in range(len(pets)):
    print(pets[i]["name"])

clinic_status = {"Clinic Status": "All animals are currently in the clinic"}
print("\nAfter adding clinic status:")
for pet in pets:
    print(pet)
print(clinic_status["Clinic Status"])
