# 5시 16분
import sys
from collections import deque
#dfs
def bfs(start, visited):
    q = deque([start])
    visited[start] = True
    
    while q:
        node = q.popleft()
        for v in graph[node]:
            if visited[v] == False:
                visited[v] = True
                q.append(v)
            
    
    

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
# print(graph)
cnt = 0
visited = [False] * (n+1)

for i in range(1, n+1):
    if visited[i] == False:
        bfs(i, visited)
        cnt += 1
# print(visited)
print(cnt)