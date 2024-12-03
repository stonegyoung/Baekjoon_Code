# 12:06
# bfs
import sys
from collections import deque

input = sys.stdin.readline

def bfs(startlist):
    sl = set(startlist)
    q = deque(startlist)
    while q:
        n = q.popleft()
        for v in graph[n]:
            if v != 1:
                sl.add(v)
    return len(sl)
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b =map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
res = bfs(graph[1]) if len(graph[1]) != 0 else 0
print(res)