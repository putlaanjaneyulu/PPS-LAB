h=input("enter list of items for home:")
o=input("enter list of items for office:")


hs = set(h.split(","))
os = set(o.split(","))
c=hs.union(os)
uh=hs.difference(os)
uo=os.difference(hs)
cu=hs.intersection(os)
print("items to buy for both:",c)
print("items to buy for home:",uh)
print("items to buy for office:",uo)
print("items common:",cu)



