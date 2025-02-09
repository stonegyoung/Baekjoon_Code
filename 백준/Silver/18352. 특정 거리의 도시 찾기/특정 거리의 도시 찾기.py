# 1:44
# bfs
import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    q = deque([start])
    visited[start] = 0
    kk = []
    while q:
        now = q.popleft()
        for v in city[now]:
            if visited[v] == -1:
                q.append(v)
                visited[v] = visited[now]+1
                if visited[v] == k:
                    kk.append(v)
    if len(kk) == 0:
        print(-1)
    else:
        for i in sorted(kk):
            print(i)
                    
n, m, k, x = map(int, input().split())
city = [[] for _ in range(n+1)]
visited = [-1] * (n+1)
for _ in range(m):
    a, b = map(int, input().split())
    city[a].append(b)
    
# print(city)
bfs(x)