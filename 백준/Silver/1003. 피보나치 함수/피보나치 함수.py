from sys import stdin

t = int(stdin.readline())
for _ in range(t):    
    n = int(stdin.readline())
    dp = [[0,0] for _ in range(n+1)]
    dp[0][0] = 1
    if n>0:
        dp[1][1] = 1
    
    for i in range(2, n+1):
        dp[i][0] = dp[i-1][0] + dp[i-2][0]
        dp[i][1] = dp[i-1][1] + dp[i-2][1]
    print(dp[n][0], dp[n][1])