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