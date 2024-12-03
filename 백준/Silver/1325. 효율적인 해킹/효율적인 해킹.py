# 1: 45
# bfs
import sys
from collections import deque

def bfs(num):
    q = deque([num])
    visited = [0] * (n+1)
    visited[num] = 1
    while q:
        node = q.popleft()
        for v in graph[node] :
            if visited[v] == 0:
                q.append(v)
                visited[v] = 1
    # print(visited)
    return sum(visited)

input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

maxi = 0
maxlist = []
for i in range(1, n+1):
    res = bfs(i)
    if maxi < res:
        maxi = res
        maxlist = [i]
    elif maxi == res:
        maxlist.append(i)
for ml in sorted(maxlist):
    print(ml, end=' ')