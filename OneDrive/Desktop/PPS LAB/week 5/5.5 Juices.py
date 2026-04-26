
juices = [
    {"flavor": "orange", "price": 50, "color": "orange"},
    {"flavor": "lemon", "price": 40, "color": "yellow"},
    {"flavor": "pomegranate", "price": 70, "color": "red"}
]

for juice in juices:
    juice["in shop"] = True

print("Initial juice list with 'in shop' status:")
print(juices[0], ",")
print(juices[1], ",")
print(juices[2])
print()

juices.append({"flavor": "grape", "price": 60, "color": "purple",
               "in shop": True})

print("After adding new juice (grape):")
print(juices[0], ",")
print(juices[1], ",")
print(juices[2], ",")
print(juices[3])
print()

total_price = 0
for juice in juices:
    total_price += juice["price"]
average_price = total_price / len(juices)

print("Average price of juices:", average_price)
