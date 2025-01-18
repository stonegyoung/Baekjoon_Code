# 4:48
# 같으면 dp[n-1][m-1] + 1
# 다르면 max(dp[n][m-1], dp[n-1][m])

import sys
input = sys.stdin.readline

str1 = input().rstrip()
str2 = input().rstrip()

M = len(str1)
N = len(str2)

dp = [[0] * (M+1) for _ in range(N+1)]

for n in range(1, N+1):
    for m in range(1, M+1):
        if str2[n-1] == str1[m-1]:
            dp[n][m] = dp[n-1][m-1] + 1
        else:
            dp[n][m] = max(dp[n-1][m], dp[n][m-1])

# print(dp)            
print(dp[n][m])