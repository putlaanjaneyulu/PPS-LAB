def maxWealth(accounts):
    return max([sum(i) for i in accounts])
accounts = [[1, 2, 3], [3,2,1]]
print(maxWealth(accounts))
