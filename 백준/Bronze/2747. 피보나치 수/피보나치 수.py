from sys import stdin

n = int(stdin.readline())


dp = [0] * (n+1)
try:
    dp[1] = 1
    dp[2] = 1
except:
    pass
for i in range(3, n+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n])