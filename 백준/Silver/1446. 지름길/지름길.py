# # 1:32
# # bfs
# import sys
# from collections import deque
# import heapq
# input = sys.stdin.readline
# INF = int(1e9)

# def dijkstra(s, visited):
#     q = []
#     heapq.heappush(q, s)
#     visited[s] = 0
#     while q:
#         v = heapq.heappop()
#         for e, d in starts[v]:
#             if distance[v]+d > distance[end]:
#                 continue
#             dis = distance[]
    
# n, d = map(int, input().split())
# distance = [INF for _ in range(10001)]
# starts = [[(1, i+1)] for i in range(10001)]
# visited = [0 for _ in range(10001)]
# for _ in range(n):
#     start, end, length = map(int, input().split())
#     if start > d or end > d:
#         continue
#     if end-start > length:
#         continue
#     starts[start].append((end, length))
    
# 1:32
# bfs
import sys
from collections import deque
import heapq
input = sys.stdin.readline
INF = int(1e9)

def bfs(fast, visited):
    q = deque([0])
    visited[0] = 0
    while q:
        s = q.popleft()
        for e, d in fast[s]:
            if e > 10000:
                continue
            if visited[s] + d < visited[e]:
                visited[e] = visited[s] + d
                q.append(e)
                
n, d = map(int, input().split())
visited = [INF for _ in range(10001)]
fast = [[(i+1, 1)] for i in range(10001)]
for _ in range(n):
    start, end, length = map(int, input().split())
    fast[start].append((end, length))
    
bfs(fast, visited)
print(visited[d])