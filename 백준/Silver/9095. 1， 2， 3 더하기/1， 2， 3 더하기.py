# 9시 5분
from sys import stdin

t = int(stdin.readline())


for _ in range(t):
    n = int(stdin.readline())
    dp = [0 for _ in range(n+1)]
    
    try:
        dp[1] = 1
        dp[2] = 2
        dp[3] = 4
    except:
        pass
    for i in range(4, n+1):
        dp[i] = dp[i-3] + dp[i-2] + dp[i-1]
    print(dp[n])