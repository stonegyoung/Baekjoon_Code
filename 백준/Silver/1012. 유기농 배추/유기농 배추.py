from sys import stdin
from collections import deque

def bfs(graph, now_x, now_y):
    queue = deque([(now_x, now_y)])
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while queue:
        now_x, now_y = queue.popleft()
        for dx, dy in direction:
            x = now_x + dx
            y = now_y + dy
            if 0<=x<n and 0<=y<m:
                if graph[x][y] == 1:
                    graph[x][y] = 0
                    queue.append((x,y))

def find_res(n, m):
    res = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                bfs(graph, i, j)
                res += 1
    print(res)

t = int(stdin.readline().rstrip())

for _ in range(t):
    # 열, 행, 배추 수
    m, n, k = map(int, stdin.readline().split())
    graph = [[0]*m for _ in range(n)]
    for _ in range(k):
        x, y =  map(int, stdin.readline().split())
        graph[y][x] = 1
        
    # print(graph)
    find_res(n, m)