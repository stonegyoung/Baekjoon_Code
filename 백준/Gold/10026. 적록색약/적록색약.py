# 6:20
# bfs

import sys
from collections import deque
input = sys.stdin.readline

def bfs(startx, starty, graph):
    q = deque([(startx, starty)])
    t = graph[startx][starty]
    graph[startx][starty] = '-'
    
    while q:
        nowx, nowy = q.popleft()
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            x = nowx + dx
            y = nowy + dy
            if 0<=x<n and 0<=y<n:
                if graph[x][y] == t:
                    q.append((x,y))
                    graph[x][y] = '-'
                
                



n = int(input())
no_rg = []
yes_rg = []
# no_visited = [[0]*n for _ in range(n)]
# yes_visited = [[0]*n for _ in range(n)]
for _ in range(n):
    st = list(input().rstrip())
    no_rg.append(st)
    
    g = []
    for s in st:
        if s == 'G':
            g.append('R')
        else:
            g.append(s)
    yes_rg.append(g)
            
    
# print(no_rg)
# print(yes_rg)

no_cnt = 0
yes_cnt = 0
for i in range(n):
    for j in range(n):
        if no_rg[i][j] in ['R', 'G', 'B']:
            bfs(i,j, no_rg)
            no_cnt += 1
        if yes_rg[i][j] in ['R', 'G', 'B']:
            bfs(i,j, yes_rg)
            yes_cnt += 1
            
print(no_cnt, yes_cnt)