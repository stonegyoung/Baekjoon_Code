# 1시 25 분
# bfs
import sys
from collections import deque
input = sys.stdin.readline

def bfs(visited):
    q = deque([(0,0,0)])
    visited[0][0][0] = 1
    
    while q:
        nowx, nowy, crush = q.popleft()
        if nowx == n-1 and nowy == m-1:
            return visited[nowx][nowy][crush]
        for dx, dy in [(-1,0), (1,0), (0,1), (0,-1)]:
            x = nowx+dx
            y = nowy+dy
            if 0<=x<n and 0<=y<m:
                if graph[x][y] == 0:
                    if visited[x][y][crush]:
                        continue
                    visited[x][y][crush] = visited[nowx][nowy][crush] + 1
                    q.append((x,y,crush))
                else:
                    if crush < k:
                        if visited[x][y][crush+1]:
                            continue
                        visited[x][y][crush+1] = visited[nowx][nowy][crush] + 1
                        q.append((x,y,crush+1))
                    else:
                        continue
    return -1
    

n, m, k = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().rstrip())))
    
visited = [[[0]*(k+1) for _ in range(m)] for _ in range(n)]
# print(visited)
res = bfs(visited)
print(res)