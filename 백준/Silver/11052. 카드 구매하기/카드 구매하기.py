# 3시 18분
# dp

import sys
input = sys.stdin.readline

n = int(input())
nlist = list(map(int, input().split()))

dp = [0] + nlist
# print(dp)
for i in range(2, n+1):
    for j in range(1, i):
        if j > i-j:
            break
        dp[i] = max(dp[i], dp[j]+dp[i-j])
        # print(dp)
        
print(dp[n])