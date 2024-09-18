# 9시 55분
from sys import stdin

t = int(stdin.readline())


for _ in range(t):
    k = int(stdin.readline()) # 층
    n = int(stdin.readline()) # 호
    
    dp = [[] for _ in range(k+1)]
    dp[0] = [i+1 for i in range(n)]
    for i in range(1, k+1):
        dp[i].append(dp[i-1][0]) # 아래층
        for j in range(1, n):
            dp[i].append(dp[i][-1] + dp[i-1][j]) # 내 옆 집+아랫집
    
    print(dp[k][n-1])    