# 4시
# dp dp[i] = 1 ~ i - 1까지의 원소들에서, i번째 원소보다 값이 작은것들 중, 가장 큰 dp값 + 1
import sys
input = sys.stdin.readline

n = int(input())
nlist = list(map(int, input().split()))
maxi = 1

dp = [1] * (n)
for i in range(1, n):
    for j in range(i):
        if nlist[j] < nlist[i]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))