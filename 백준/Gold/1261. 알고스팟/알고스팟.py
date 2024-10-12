# 10시 32분

import sys
from collections import deque
input = sys.stdin.readline
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
                if graph[x][y] == 1:
                    if visited[x][y] == -1:
                        visited[x][y] = visited[nowx][nowy]+1
                        q.append((x,y))
                    else:
                        if visited[x][y] > visited[nowx][nowy]+1:
                            visited[x][y] = visited[nowx][nowy]+1
                            q.append((x,y))
                elif graph[x][y] == 0:
                    if visited[x][y] == -1:
                        visited[x][y] = visited[nowx][nowy]
                        q.append((x,y))
                    else:
                        if visited[x][y] > visited[nowx][nowy]:
                            visited[x][y] = visited[nowx][nowy]
                            q.append((x,y))
graph = []
for _ in range(m):
    graph.append(list(map(int, input().rstrip())))
visited = [[-1]* n for _ in range(m)]

bfs(0,0)
print(visited[m-1][n-1])