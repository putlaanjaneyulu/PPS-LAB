def runningSum(num):
    for i in range(1,len(num)):
        num[i]=num[i]+num[i-1]
    return num
num=[1,2,3,4]
print(runningSum(num))
