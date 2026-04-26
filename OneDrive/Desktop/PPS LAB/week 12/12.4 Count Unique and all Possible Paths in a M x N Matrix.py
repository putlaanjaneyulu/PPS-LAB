'''def count_paths(m, n):
    # Base case: If only one row or one column, only one path exists
    if m == 1 or n == 1:
        return 1
    # Recursive case: Move down (m-1, n) and right (m, n-1)
    return count_paths(m - 1, n) + count_paths(m, n - 1)
# Sample Inputs
M = 3
N = 4
print("Number of unique paths:", count_paths(M, N)) '''
#
def count_paths_dp(m, n):
    dp = [[0 for _ in range(n)] for _ in range(m)]
    # Fill first row and column
    for i in range(m):
        dp[i][0] = 1
    for j in range(n):
        dp[0][j] = 1
    # Fill remaining cells
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[m-1][n-1]
# Example
print(count_paths_dp(3,4))  
