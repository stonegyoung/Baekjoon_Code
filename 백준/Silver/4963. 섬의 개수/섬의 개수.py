# 10 29qns
import sys
input = sys.stdin.readline
from collections import deque

def bfs(startx, starty):
    q = deque([(startx, starty)])
    graph[startx][starty] = 0
    while q:
        nowx, nowy = q.popleft()
        for dx, dy in [(-1,0), (1,0), (0,1), (0,-1), (-1,-1), (1,-1), (-1,1), (1,1)]:
            x = nowx+dx
            y = nowy+dy
            if 0<=x<h and 0<=y<w:
                if graph[x][y] ==1:
                    graph[x][y] = 0
                    q.append((x,y))

while True:
    w, h = map(int, input().split())
    if w==0 and h==0:
        break
    else:
        graph = []
        for _ in range(h):
            graph.append(list(map(int, input().split())))
        # print(graph)
        
        cnt = 0
        for i in range(h):
            for j in range(w):
                if graph[i][j] == 1:
                    bfs(i, j)
                    cnt += 1
        print(cnt)