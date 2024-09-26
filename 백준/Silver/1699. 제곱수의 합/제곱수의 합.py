from math import sqrt
import sys

input = sys.stdin.readline

n = int(input())
dp = [0] * (n+1)
dp[0] = 0
dp[1] = 1

# -제곱수 + 1 중 찾기'
for k in range(1, n+1):
    dp[k] = dp[k-1] + 1
    for i in range(2, int(sqrt(k))+1):
        dp[k] = min(dp[k], dp[k-(i**2)]+1)
print(dp[n])