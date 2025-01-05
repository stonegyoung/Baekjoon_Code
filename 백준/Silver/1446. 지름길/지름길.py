# 1:32
# bfs
import sys
from collections import deque
input = sys.stdin.readline
# INF = int(1e9)

# def bfs(fast, visited):
#     q = deque([0])
#     visited[0] = 0
#     while q:
#         s = q.popleft()
#         for e, d in fast[s]:
#             if e > 10000:
#                 continue
#             if visited[s] + d < visited[e]:
#                 visited[e] = visited[s] + d
#                 q.append(e)
                
# n, d = map(int, input().split())
# visited = [INF for _ in range(10001)]
# fast = [[(i+1, 1)] for i in range(10001)]
# for _ in range(n):
#     start, end, length = map(int, input().split())
#     fast[start].append((end, length))
    
# bfs(fast, visited)
# print(visited[d])

n, d = map(int, input().split())
dp = [i for i in range(10001)]
fast = []
for _ in range(n):
    start, end, length = map(int, input().split())
    fast.append((start, end, length))
for i in range(d+1):
    if i > 0:
        dp[i] = min(dp[i],dp[i-1]+1)
    for s, e, l in fast:
        if dp[s]+l < dp[e]:
            dp[e] = dp[s]+l
print(dp[d])