
tshirt = {
    "Color": "Red",
    "Size": "M",
    "Neck Type": "Round"
}

print("a. Initial T-shirt information:")
print(tshirt)


tshirt["Quantity"] = 25                  
tshirt.update({"Logo Color": "Blue"})   

print("b. After adding quantity and logo color:")
print(tshirt)


tshirt["Sold"] = 20

print("c. After recording sales:")
print(tshirt)


tshirt["Quantity"] = tshirt["Quantity"] - tshirt["Sold"]

print("d. After updating remaining quantity:")
print(tshirt)
