# 1tl 18qns
# n 행
# m 열
# 2에서 시작
# bfs
import sys
input = sys.stdin.readline
from collections import deque
n, m = map(int, input().split())
graph = []
start = ()
visited = [[-1]*m for _ in range(n)]
for i in range(n):
    lists = list(map(int, input().split()))
    for j in range(m):
        if lists[j] == 0:
            visited[i][j] = 0
        if lists[j] == 2:
            start = (i,j)
    graph.append(lists)
# print(start)
# print(graph)

def bfs(start):
    q = deque([start])
    visited[start[0]][start[1]] = 0
    
    while q:
        nowx, nowy = q.popleft()
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            x = nowx+dx
            y = nowy+dy
            
            if 0<=x<n and 0<=y<m:
                if visited[x][y] == -1:
                    if graph[x][y] == 1:
                        visited[x][y] = visited[nowx][nowy]+1
                        q.append((x,y))

bfs(start)
# print(visited)
for visit in visited:
    for v in visit:
        print(v, end=' ')
    print()