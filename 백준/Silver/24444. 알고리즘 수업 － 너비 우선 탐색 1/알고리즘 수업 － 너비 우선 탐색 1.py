# 2시 13분
import sys
from collections import deque

input = sys.stdin.readline

i = 1
def bfs(visited, E, R):
    global i
    visited[R] = i
    queue = deque([R])
    while queue:
        u = queue.popleft()

        for v in sorted(E[u]):
            if visited[v] == False:
                i+=1
                visited[v] = i
                queue.append(v)
    

n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    
    graph[u].append(v)
    graph[v].append(u)
  
visited = [0] * (n+1)
bfs(visited, graph, r) 
for i in range(1, n+1):
    print(visited[i]) 
