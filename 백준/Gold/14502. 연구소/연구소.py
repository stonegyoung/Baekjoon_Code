#40qns~
import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    visited = [[0]*m for _ in range(n)]
    q = deque(start)
    for s in start:
        visited[s[0]][s[1]] = 1
    cnt = 0
    while q:
        nowx, nowy = q.popleft()
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            x = nowx+dx
            y = nowy+dy
            if 0<=x<n and 0<=y<m:
                if graph[x][y] == 0 and visited[x][y] == 0:
                    cnt += 1
                    visited[x][y] = 1
                    q.append((x,y))
    # print(visited)
    return length-cnt-3
    
    
n, m = map(int, input().split())
graph = []
virus = []
wall = []
empty = []
for i in range(n):
    lists = list(map(int, input().split()))
    graph.append(lists)
    for j in range(m):
        if graph[i][j] == 2:
            virus.append((i,j))
        elif graph[i][j] == 1:
            wall.append((i,j))
        else:
            empty.append((i,j))
length = len(empty)
# print(length)
maxi = 0
for i in range(length):
    for j in range(i+1, length):
        for k in range(j+1, length):
            graph[empty[i][0]][empty[i][1]] = 1
            graph[empty[j][0]][empty[j][1]] = 1
            graph[empty[k][0]][empty[k][1]] = 1
            maxi = max(maxi, bfs(virus))
            graph[empty[i][0]][empty[i][1]] = 0
            graph[empty[j][0]][empty[j][1]] = 0
            graph[empty[k][0]][empty[k][1]] = 0
            
print(maxi)