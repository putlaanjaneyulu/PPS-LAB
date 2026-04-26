V, I = map(int, input("enter positive integers for V and I:").split(","))
t = int(input("Enter time:"))
P = V * I
E = P * t
print(f"Power: {P} W")
print(f"Energy: {E} Wh")
