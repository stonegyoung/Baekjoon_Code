import sys
input = sys.stdin.readline

n = int(input())
gp = [0] + [int(input()) for _ in range(n)]

dp = [0] * (n+1)
try:
    dp[1] = gp[1]
    dp[2] = gp[1] + gp[2]
except:
    pass
for i in range(3, n+1):
    maxi = max(dp[:i-2])
    dp[i] = gp[i] + max(gp[i-1]+maxi, max(maxi, dp[i-2])) # 직전 거 먹었을 때/ 지지난 거 먹었을 때
# print(dp)
print(max(dp))    