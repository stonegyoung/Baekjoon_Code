# 3시 50분
# 1 1 1 2 2 (2+1) (3+1) (4+1) (5+2) (7+2) (9+3) (12+4)
# dp

import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    dp = [0] * (n+1)
    
    dp[1] = 1
    try:
        dp[2] = 1
        dp[3] = 1
        dp[4] = 2
        dp[5] = 2
    except:
        pass
    
    for i in range(6, n+1):
        dp[i] = dp[i-1] + dp[i-5]
        
    print(dp[n])