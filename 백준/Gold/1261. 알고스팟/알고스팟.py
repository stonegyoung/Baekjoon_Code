# 10시 32분~51분

import sys
from collections import deque
import heapq
input = sys.stdin.readline
INF = int(1e9)
# n은 열 m은 행
n, m = map(int, input().split())

def bfs(x,y):
    q = deque([(x,y)])
    visited[x][y] = 0
    while q:
        nowx, nowy = q.popleft()
        for dx, dy in [(-1,0), (1,0), (0,1), (0,-1)]:
            x = nowx+dx
            y = nowy+dy
            
            if 0<=x<m and 0<=y<n:
                    if visited[x][y] == -1:
                        visited[x][y] = visited[nowx][nowy]+graph[x][y]
                        q.append((x,y))
                    else:
                        if visited[x][y] > visited[nowx][nowy]+graph[x][y]:
                            visited[x][y] = visited[nowx][nowy]+graph[x][y]
                            q.append((x,y))
                            
def dijkstra(x,y):
    q = []
    heapq.heappush(q, (graph[x][y],x,y))
    distances[x][y] = graph[x][y]
    while q:
        cost, nowx, nowy = heapq.heappop(q)
        
        if cost > distances[nowx][nowy]:
            continue
        for dx, dy in [(-1,0), (1,0), (0,1), (0,-1)]:
            x = nowx+dx
            y = nowy+dy
            
            if 0<=x<m and 0<=y<n:
                dist = cost + graph[x][y]
                if dist < distances[x][y]:
                    distances[x][y] = dist
                    heapq.heappush(q, (dist, x, y))
        
    
graph = []
for _ in range(m):
    graph.append(list(map(int, input().rstrip())))
visited = [[-1]* n for _ in range(m)]
distances = [[INF]* n for _ in range(m)]

# bfs(0,0)
# print(visited[m-1][n-1])
dijkstra(0,0)
print(distances[m-1][n-1])