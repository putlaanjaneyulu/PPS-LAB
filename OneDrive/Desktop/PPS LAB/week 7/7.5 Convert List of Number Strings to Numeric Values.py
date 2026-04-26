def ToNumbers(strlist):
    for i in range(len(strlist)):
        strlist[i]=float(strlist[i])
strlist=input("Enter an integer").split()
ToNumbers(strlist)
print(strlist)
