# 9시 25분
from sys import stdin

n = int(stdin.readline())

data = []
for _ in range(n):
    data.append(list(map(int, stdin.readline().split())))
    
dp = [[0]*i for i in range(1, n+1)]
dp[0] = data[0]
for i in range(n-1):
    for j in range(len(data[i])):
        # 인덱스 인덱스+1 
        dp[i+1][j] = max(dp[i][j]+data[i+1][j], dp[i+1][j])
        dp[i+1][j+1] = max(dp[i][j]+data[i+1][j+1], dp[i+1][j+1])
print(max(dp[n-1]))