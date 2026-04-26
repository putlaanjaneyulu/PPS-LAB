
a = set(input("Enter participants in Event A: ").split())
b = set(input("Enter participants in Event B: ").split())

both = a & b

only_one = a.symmetric_difference(b) 

print("Participants registered for both events:", both)
print("Participants registered for only one event:", only_one)
