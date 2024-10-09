# 10시 37분
import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    q = deque(start)
    while q:
        nowx, nowy = q.popleft()
        nowxy = graph[nowx][nowy]
        for dx, dy in directions:
            x= nowx+dx
            y = nowy + dy
            if 0<=x<m and 0<=y<n:
                cost = graph[x][y]
                if cost == 0:
                    graph[x][y] = nowxy + 1
                    q.append([x,y])
                elif cost != -1 and cost > nowxy+1:
                    graph[x][y] = nowxy + 1
                    q.append([x,y])

def return_max(graph, where):
    if len(where) != 0:
        bfs(where)
    maxi = 0
    for i in range(m):
        for j in range(n):
            if graph[i][j] == 0:
                return -1      
            maxi = max(graph[i][j], maxi)
    return maxi-1        
    

# 가로(열) 세로(행)
n, m = map(int, input().split())

directions = [(1,0), (-1,0), (0,1), (0,-1)]

graph = []
where = []
for i in range(m):
    a = list(map(int, input().split()))
    for j in range(n):
        if 1 == a[j]:
            where.append([i,j])
    graph.append(a)
    
            
print(return_max(graph, where)) # 나중에 -1 해준다