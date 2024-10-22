import sys
input = sys.stdin.readline

n, k = map(int, input().split())
wv = [[]]
for _ in range(n):
    w, v= map(int, input().split())
    wv.append((w,v))
    
# 냅색 점화식
# ns(n, w) = max(ns(n-1, w), ns(n-1, w-wv[i][0])+wv[i][1])

# 행: 들어가는 가방 수
# 열: 무게 수
dp = [[0]*(k+1) for _ in range(n+1)]

for i in range(1, n+1):
    w, v = wv[i]
    for j in range(1, k+1):
        if w > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] +v) # 지금 가방 안들었을 때, 지금 가방 들었을 때
print(dp[n][k])