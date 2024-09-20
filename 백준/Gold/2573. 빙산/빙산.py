# 10시 18분~10tl30
# 10시 45분 11시 35qns

# 상하좌우 -> 몇인지 넣을 리스트
# 두 덩어리 이상이 되는 지 확인 분리 되는 지 확인 안되면 0 -> bfs

import sys
from collections import deque
input = sys.stdin.readline

def count_0(nowx, nowy):
    cnt = 0
    for dx, dy in direction:
        x = nowx + dx
        y = nowy + dy
        if 0<=x<n and 0<=y<m:
            if graph[x][y] == 0:
                cnt += 1
    return cnt

def dfs(graph, visited, nowx, nowy):
    queue = deque([(nowx, nowy)])
    visited[nowx][nowy] = False # 들르면 False
    
    while queue:
        nowx, nowy = queue.popleft()
        for dx, dy in direction:
            x = nowx + dx
            y = nowy + dy
            if 0<=x<n and 0<=y<m:
                if graph[x][y] != 0 and visited[x][y] == True:
                        queue.append((x,y))
                        visited[x][y] = False
                        

# 행 열
n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
    
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
       
nonzero = {}
for i in range(n):
    for j in range(m):
        if graph[i][j] != 0:
            nonzero[(i,j)] = count_0(i,j)
            
result = 0
cnt = 0
while graph != [[0]*m for _ in range(n)]:
    # 좌표와 빙산이 - 되는 걸 같이 적는 리스트 
    # 좌표 중에 -했더니 녹은 거면 그 근처 애들 카운트 다시
    for x, y in nonzero:
        graph[x][y] = max(0, graph[x][y] - nonzero[(x,y)])
    for x, y in nonzero:
        if graph[x][y] != 0:
            nonzero[(x,y)] = count_0(x,y) # 다시 업데이트
    cnt += 1
    visited = [[True]*m for _ in range(n)]
    
    res = 0
    for i in range(n):
        for j in range(m):
            if visited[i][j]==True and graph[i][j]!=0:
                dfs(graph, visited, i,j) 
                res += 1
                # print(i, j)
    if res > 1:
        result = cnt
        break
print(result)