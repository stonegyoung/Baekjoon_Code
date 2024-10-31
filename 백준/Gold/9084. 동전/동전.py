# 3tl 46qns

# dp
import sys
input= sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    money = list(map(int, input().split()))
    m = int(input())
    dp = [[0]*(m+1)]
    
    for mon in money:
        d = [0]*(m+1)
        i = 1
        r = mon * i
        while r <= m:
            d[r] = 1
            i += 1
            r = mon * i
        dp.append(d)
    
    # print(dp)
    
    for i in range(1, n+1):
        now = dp[i]
        last = dp[i-1]
        mon = money[i-1]
        for j in range(1, m+1):
            if j < mon:
                now[j] = last[j]
            elif j == mon:
                now[j] = last[j] + 1
            else:
                now[j] = last[j] + now[j-mon] 
    print(dp[-1][-1])