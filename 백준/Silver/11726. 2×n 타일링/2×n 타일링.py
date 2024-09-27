# 11시 28분
# dp

import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * (n+1)
dp[1] = 1
if n != 1:
    dp[2] = 2

for i in range(3, n+1):
    # dp[i-1]에 1*2 타일 하나(한 가지), dp[i-2]에 2*1 타일 두 개(한 가지)
    dp[i] = (dp[i-1] + dp[i-2])%10007
    
print(dp[n])