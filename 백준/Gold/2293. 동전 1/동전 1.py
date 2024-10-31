# 6시 27분
# 무한 배낭
import sys
input = sys.stdin.readline
n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))
    
dp = [0] * (k+1)
dp[0] = 1 # 아무 동전을 사용하지 않는 경우 1

for coin in coins:
    for i in range(coin, k+1):
        dp[i] += dp[i-coin]
        
print(dp[-1])