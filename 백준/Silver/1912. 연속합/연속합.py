# 4시 24분
import sys
input = sys.stdin.readline

n = int(input())

seq = list(map(int, input().split()))

dp = [0] * n
dp[0] = seq[0]

# -만 아니면 계속 하는 게 낫다
for i in range(1, n):
    if dp[i-1] > 0:
        dp[i] = dp[i-1] + seq[i]
    else:
        dp[i] = seq[i]
        
print(max(dp))