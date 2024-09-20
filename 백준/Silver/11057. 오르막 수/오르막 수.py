# 3시 49분
# 같으면 오름차순

import sys

input = sys.stdin.readline

n = int(input())

dp = [1] * 10 # 0~9가 나오는 수 # 0은 한 번 1은 두 번
for _ in range(2, n+1):
    for i in range(1, 10): # 맨 뒷자리에 i가 몇 번 나올 수 있나
        dp[i] = dp[i] + dp[i-1]
    
# print(dp)
print(sum(dp)%10007)