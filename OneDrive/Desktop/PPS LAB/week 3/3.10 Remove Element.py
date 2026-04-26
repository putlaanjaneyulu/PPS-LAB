def removeElement(num,val):
    index=0
    for i in range(len(num)):
        if num[i]!=val:
            num[index]=num[i]
            index+=1
    return index
num=[1,2,3,4]
val=3
print(removeElement(num,val))

