
a = input("Enter cities visited by Person A (comma-separated): ")
b = input("Enter cities visited by Person B (comma-separated): ")
sa = set(map(str.strip, a.split(",")))
sb = set(map(str.strip, b.split(",")))

c = sa.intersection(sb)   
ua = sa.difference(sb)   
ub = sb.difference(sa)    
u = sa.union(sb)       


print("Cities visited by both:", c)
print("Cities unique to Person A:", ua)
print("Cities unique to Person B:", ub)
print("All cities visited:", u)
