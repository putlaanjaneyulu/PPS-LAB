def twosum(n,t):
    for i in range(len(n)):
        for j in range(len(n)):
            if i!=j and n[i]+n[j]==t:
                return[i,j]



        
n =  [3, 2, 4]
t = 6
print(twosum(n,t))
