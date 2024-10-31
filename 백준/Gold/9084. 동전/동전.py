import sys
input= sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    money = list(map(int, input().split()))
    m = int(input())
    
    dp = [0] * (m+1)
    dp[0] = 1
    for mon in money:
        for i in range(mon, m+1):
            dp[i] += dp[i-mon]
    print(dp[-1])