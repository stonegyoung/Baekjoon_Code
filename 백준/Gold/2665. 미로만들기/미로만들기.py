# 11 21
# bfs
# 1이면 다 0으로 초기화 1이면 +1

import sys
import heapq
from collections import deque
INF = int(1e9)
input = sys.stdin.readline

def bfs(startx, starty):
    q = deque([(startx, starty)])
    visited[startx][starty] = 0
    while q:
        nowx, nowy = q.popleft()
        for dx, dy in [(-1,0), (1,0), (0,1), (0,-1)]:
            x = nowx+dx
            y = nowy+dy
            if 0<=x<n and 0<=y<n:
                last = visited[nowx][nowy]
                if graph[x][y] == 1:
                    if visited[x][y] == -1: # -1이고 visit x
                        visited[x][y] = last
                        q.append((x,y))
                    else :
                        if visited[x][y] > last:
                            visited[x][y] = last
                            q.append((x,y))
                else:
                    if visited[x][y] == INF:
                        visited[x][y] = last + 1
                        q.append((x,y))
                    else :
                        if visited[x][y] > last+1:
                            visited[x][y] = last+1
                            q.append((x,y))
    return visited[n-1][n-1]
                
        
n=int(input())
graph = []
visited = []
for _ in range(n):
    lists = list(map(int, input().rstrip()))
    graph.append(lists)
    g = []
    for i in lists:
        if i == 1:
            g.append(-1)
        else:
            g.append(INF)
    visited.append(g)

a = bfs(0,0)
print(a)
# print(visited)