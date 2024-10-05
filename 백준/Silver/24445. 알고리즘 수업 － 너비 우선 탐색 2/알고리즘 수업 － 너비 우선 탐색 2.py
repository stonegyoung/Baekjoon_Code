# 2시 56분
# bfs

import sys
from collections import deque
input = sys.stdin.readline

def bfs(start, graph, visited):
    cnt = 1
    
    q = deque([start])
    visited[start] = cnt
    cnt +=1
    while q:
        node = q.popleft()
        for n in graph[node]:
            if visited[n] == 0:
                visited[n] = cnt
                cnt += 1
                q.append(n)
                

n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    
for g in graph:
    g.sort(reverse=True)
    
# print(graph)

bfs(r, graph, visited)
# print(visited)
for v in visited[1:]:
    print(v)