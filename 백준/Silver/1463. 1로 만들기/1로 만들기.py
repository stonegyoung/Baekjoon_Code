from sys import stdin

x = int(stdin.readline())

dp = [100000000]*(x+1)
dp[0], dp[1] = 0, 0
for i in range(2, x+1):
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3]+1)
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1)
    dp[i] = min(dp[i], dp[i-1]+1)
    
print(dp[x])