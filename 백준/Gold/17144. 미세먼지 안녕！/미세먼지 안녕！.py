# 38분
import sys
input = sys.stdin.readline
from collections import deque

def bfs(starts): # 미세먼지 있는 노드들 다
    new_mm = set()
    q = deque(starts)
    while q:
        nowx, nowy = q.popleft()
        a = graph[nowx][nowy]
        if a < 5:
            new_mm.add((nowx, nowy))
            continue
        sp = a//5
        cnt = 0
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            x = nowx+dx
            y = nowy+dy
            if 0<=x<r and 0<=y<c:
                if graph[x][y] != -1:
                    visited[x][y] += sp
                    cnt += 1
                    new_mm.add((x,y))
        graph[nowx][nowy] -= sp*cnt
        new_mm.add((nowx,nowy))
    return new_mm

def cycle(air, graph, mm):
    a, b = air
    if a > b:
        a, b = b, a # a가 위, b가 아래
    # 위에
    for i in range(a-1, 0, -1):
        graph[i][0] = graph[i-1][0]
        mm.add((i,0))
    aa0 = graph[0]
    for i in range(0, c-1):
        aa0[i] = aa0[i+1]
        mm.add((0,i))
    for i in range(0, a):
        graph[i][c-1] = graph[i+1][c-1]
        mm.add((i, c-1))
    aa = graph[a]
    for i in range(c-1, 1, -1):
        aa[i] = aa[i-1]
        mm.add((a,i))
    aa[1] = 0

    # 아래
    for i in range(b+1, r-1):
        graph[i][0] = graph[i+1][0]
        mm.add((i, 0))
    bbr = graph[r-1]
    for i in range(0, c-1):
        bbr[i] = bbr[i+1]
        mm.add((r-1, i))
    for i in range(r-1, b,-1):
        graph[i][c-1] =graph[i-1][c-1] 
        mm.add((i, c-1))
    bb = graph[b]
    for i in range(c-1, 1,-1):
        bb[i] = bb[i-1] 
        mm.add((b,i))
    bb[1] = 0
    


r, c, t = map(int, input().split())
graph = []
mm = []
air = []
for i in range(r):
    lists = list(map(int, input().split()))
    if lists[0] == -1:
        air.append(i)
    for j in range(c):
        if lists[j] != 0 and lists[j] != -1:
            mm.append([i,j])
    graph.append(lists)

# 1초마다
for _ in range(t):
    visited= [[0]*c for _ in range(r)]
    mm = bfs(mm)
    for i in range(r):
        for j in range(c):
            graph[i][j] += visited[i][j]
        
    cycle(air, graph, mm)
# print(graph)
total = 0
for i, j in mm:
    total += graph[i][j]
print(total)