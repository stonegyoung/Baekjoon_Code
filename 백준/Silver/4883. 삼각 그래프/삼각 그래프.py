# 10:48
import sys
input = sys.stdin.readline
t = 1
while True:
    n = int(input())
    total = 0
    if n == 0:
        break
    graph = [list(map(int, input().split())) for _ in range(n)]
    g0 = graph[0]
    dp = [1000001, g0[1], g0[1]+g0[2]]
    for g in graph[1:-1]:
        a = min(dp[0], dp[1]) + g[0]
        b = min(dp[0], dp[1], dp[2], a) + g[1]
        c = min(dp[1], dp[2], b) + g[2]
        dp = [a,b,c]
    glast = graph[-1] 
    total = min(dp[0]+glast[0], dp[1]+glast[0], dp[0], dp[1], dp[2]) +glast[1]
    
    print(f'{t}. {total}')
    t += 1
    