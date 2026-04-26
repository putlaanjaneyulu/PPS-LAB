def plusone(d):
    if d[-1]<9:
        d[-1]+=1
        return d
    elif len(d)==1 and d[0]==9:
        return [1,0]
    # else:
    #     d[-1]=0
    #     d[0:-1]= plusone(d[0:-1])
    #     return d
    
d=[9,9]
print(plusone(d))

