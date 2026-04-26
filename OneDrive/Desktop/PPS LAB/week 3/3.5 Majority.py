def majorityElement(num):
    n=len(num)
    for i in num:
        if num.count(i)>n/2:
            return i
num=[1,2,1]
print(majorityElement(num))

