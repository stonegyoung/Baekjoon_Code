# 3시 49분
# 같으면 오름차순

import sys

input = sys.stdin.readline

n = int(input())

dp = [[0]* 10] * (n+1)
dp[1] = [1 for i in range(10)] # 0~9가 나오는 수 # 0은 한 번
for i in range(2, n+1):
    lists = []
    for j in range(10):
        lists.append(sum(dp[i-1][:j+1]), )
    dp[i] = lists
    
print(sum(dp[n])%10007)