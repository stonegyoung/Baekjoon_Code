# 10:20
import sys
from collections import deque
input = sys.stdin.readline

knight = [(-2,1), (-1,2), (1,2), (2,1), (2,-1), (1,-2),(-1,-2),(-2,-1)]
def bfs(visited, startx, starty, targetx, targety):
    q = deque([(startx, starty)])
    visited[startx][starty] = 1
    while q:
        nowx, nowy = q.popleft()
        if nowx == targetx and nowy == targety:
            return visited[nowx][nowy]-1
        for dx, dy in knight:
            x = nowx+dx
            y = nowy+dy
            if 0<=x<l and 0<=y<l and visited[x][y]==0:
                visited[x][y] = visited[nowx][nowy] + 1 
                q.append((x,y))

t = int(input())
for _ in range(t):
    l = int(input())
    visited = [[0]*l for _ in range(l)]
    nowx, nowy = map(int, input().split())
    wantx, wanty = map(int, input().split())
    if nowx==wantx and nowy==wanty:
        print(0)
    else:
        res = bfs(visited, nowx, nowy, wantx, wanty)
        print(res)