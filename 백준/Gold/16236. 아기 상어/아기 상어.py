# 4:00
import sys
from collections import deque
input = sys.stdin.readline

# def bfs(start):
#     global sh_shape, eat
#     cnt = 0
#     q = deque([start])
#     graph[start[0]][start[1]] = 0
#     while q:
#         nowx, nowy = q.popleft()
#         if graph[nowx][nowy] < sh_shape:
#             graph[nowx][nowy] = 0
#             eat += 1
            
#             if eat == sh_shape:
#                 eat = 0
#                 sh_shape += 1
            
#         # 숫자 보기
#         for dx, dy in [(-1,0), (0,-1), (1,0), (0,1)]:
#             x = nowx + dx
#             y = nowy + dy
#             if 0<=x<n and 0<=y<n and graph[x][y] <= sh_shape:
#                 q.append((x,y))
#                 cnt += 1
                
#     return cnt
              
def bfs(startx, starty):
    visited = [[0]*n for _ in range(n)]
    q = deque([(startx, starty)])
    visited[startx][starty] = 1
    cand = []
    while q:
        nowx, nowy = q.popleft()

        # 숫자 보기
        for dx, dy in [(-1,0), (0,-1), (1,0), (0,1)]:
            x = nowx + dx
            y = nowy + dy

            if 0<=x<n and 0<=y<n and visited[x][y] == 0:
                g = graph[x][y]
                if g == 0:
                    visited[x][y] = visited[nowx][nowy]+1
                    q.append((x,y))
                elif g < sh_shape:
                    visited[x][y] = visited[nowx][nowy]+1
                    cand.append((visited[x][y]-1, x, y))
                elif g == sh_shape:
                    visited[x][y] = visited[nowx][nowy]+1
                    q.append((x,y))
    return sorted(cand, key = lambda x: (x[0], x[1], x[2]))

sh_shape = 2
eat = 0

n = int(input())
shape = [[] for _ in range(7)]
graph = []
shape = set()
for i in range(n):
    l = list(map(int, input().split()))
    graph.append(l)
    
    for j in range(n):
        if l[j] == 9:
            babyx, babyy = i,j
        if l[j] in [1, 2, 3, 4, 5, 6]:
            shape.add((i,j))
    
cnt = 0
eat = 0
while True:
    v = bfs(babyx, babyy)
    if len(v) == 0:
        print(cnt)
        break
    else:
        # print(v)
        cnt += v[0][0]
        eat += 1
        graph[babyx][babyy] = 0
        babyx, babyy = v[0][1], v[0][2]
        
        if eat == sh_shape:
            sh_shape += 1
            eat = 0
  