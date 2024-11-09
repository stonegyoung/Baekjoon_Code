# 11 21~12시 25분
# bfs
# 1이면 다 0으로 초기화 1이면 +1

import sys
import heapq
from collections import deque
INF = int(1e9)
input = sys.stdin.readline

def dijkstra(startx, starty):
    q = []
    heapq.heappush(q, (0,startx,starty))
    visited[startx][starty] = 0
    while q:
        last, nowx, nowy = heapq.heappop(q)
        for dx, dy in [(-1,0), (1,0), (0,1), (0,-1)]:
            x = nowx+dx
            y = nowy+dy
            if 0<=x<n and 0<=y<n:
                if last > visited[x][y]:
                    continue
                if graph[x][y] == 1:                        
                    if last < visited[x][y]:
                        visited[x][y] = last
                        heapq.heappush(q, (last,x,y))
                else:
                    if last+1 < visited[x][y]:
                        visited[x][y] = last+1
                        heapq.heappush(q, (last+1,x,y))
    return visited[n-1][n-1]
n=int(input())
graph = []
visited = [[INF]*n for _ in range(n)]
for _ in range(n):
    lists = list(map(int, input().rstrip()))
    graph.append(lists)

a = dijkstra(0,0)
# print(visited)
print(a)