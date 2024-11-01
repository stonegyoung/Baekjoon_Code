import sys
input = sys.stdin.readline

n = int(input())
nlist = [0] + list(map(int, input().split()))

dp = [0 for _ in range(n+1)]

dp[1] = nlist[1]
for i in range(2, n+1):
    for j in range(i):
        if nlist[j] < nlist[i]:
            dp[i] = max(dp[i], dp[j]+nlist[i])
    
print(max(dp))