# 4시 43분
# dp 뒤에서부터
import sys
input = sys.stdin.readline

n = int(input())
T, P = [0]*(n+1), [0]*(n+1)
dp = [0]*(n+1)
for i in range(1, n+1):
    a, b = map(int, input().split())
    T[i] = a
    P[i] = b
    
for i in range(n, 0, -1):
    afterday = i + (T[i]-1)
    if afterday < n:
        dp[i] = P[i] + max(dp[afterday+1:])
        pass
    elif afterday == n:
        dp[i] = P[i]
print(max(dp))