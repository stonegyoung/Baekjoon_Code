# dfs/bfs
# 상태값도 0 가로 1 세로 2 대각선
import sys
from collections import deque
input = sys.stdin.readline

def go0(nowx, nowy, q):
    x = nowx
    y = nowy+1
    if 0<=x<n and 0<=y<n:
        if graph[x][y] == 0 :
            q.append((x,y,0))
        
def go1(nowx, nowy, q):
    x = nowx+1
    y = nowy
    if 0<=x<n and 0<=y<n:
        if graph[x][y] == 0 :
            q.append((x,y,1))
        
def go2(nowx, nowy, q):
    x = nowx+1
    y = nowy+1
    if 0<=x<n and 0<=y<n:
        if graph[nowx+1][nowy] == 0 and graph[nowx][nowy+1] == 0 and graph[x][y] == 0:
            q.append((x,y,2))
                
def dfs(start):
    q = deque([start])
    cnt = 0
    while q:
        nowx, nowy, state = q.pop()
        if nowx == n-1 and nowy==n-1:
            cnt += 1
            continue
        if state == 0: # 가로
            go0(nowx, nowy, q)
            go2(nowx, nowy, q)
        elif state == 1: # 세로
            go1(nowx, nowy, q)
            go2(nowx, nowy, q) 
        else: # 대각선
            go0(nowx, nowy, q)
            go1(nowx, nowy, q)
            go2(nowx, nowy, q)
    return cnt

n = int(input())
graph = []
visited = [[0]*n for _ in range(n)]
for _ in range(n):
    graph.append(list(map(int, input().split())))
    

cnt = dfs((0,1,0))
# print(visited)
print(cnt)