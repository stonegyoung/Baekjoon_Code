# 4:00
import sys
from collections import deque
input = sys.stdin.readline
              
def bfs(startx, starty):
    visited = [[0]*n for _ in range(n)]
    q = deque([(startx, starty)])
    visited[startx][starty] = 1
    cand = []
    while q:
        nowx, nowy = q.popleft()

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

n = int(input())
graph = []
for i in range(n):
    l = list(map(int, input().split()))
    graph.append(l)
    
    for j in range(n):
        if l[j] == 9:
            babyx, babyy = i,j
    
sh_shape = 2
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
  