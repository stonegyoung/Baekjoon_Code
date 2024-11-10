# 10tl 18
# bfs
import sys
input = sys.stdin.readline
from collections import deque

def bfs(startx, starty):
    q = deque([(startx,starty)])
    graph[startx][starty] = 0
    cnt = 1
    while q:
        nowx, nowy = q.popleft()
        for dx, dy in [(-1,0), (1,0), (0,1), (0,-1)]:
            x = nowx+dx
            y = nowy+dy
            if 0<=x<n and 0<=y<m:
                if graph[x][y] == 0:
                    continue
                else:
                    cnt += 1
                    graph[x][y] = 0
                    q.append((x,y))
    return cnt

n, m = map(int, input().split())
graph = []
for _ in range(n):
    lists = list(map(int, input().split()))
    graph.append(lists)
    
# print(graph)

cnt = 0
maxi = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            cnt += 1
            maxi = max(maxi, bfs(i,j))
print(cnt)
print(maxi)