tshirt = input().split(",")
tshirt = [item.strip() for item in tshirt]
new_text = input().strip()


index = tshirt.index("add your text here")
print('Position of "add your text here":', index)


tshirt = [new_text if item == "add your text here" else item for item in tshirt]
print("Updated T-shirt characteristics:", tshirt)
