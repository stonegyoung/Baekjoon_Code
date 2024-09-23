import sys
input = sys.stdin.readline

n = int(input())

lists = [[]]
for _ in range(n):
    rgb = list(map(int, input().split())) # (순위, 비용)
    lists.append(rgb)
    
dp = [[0]*3 for _ in range(n+1)]
dp[1] = lists[1]
for i in range(2, n+1):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + lists[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + lists[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + lists[i][2]
    
print(min(dp[n]))
