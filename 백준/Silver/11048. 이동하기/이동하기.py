# 4시 36분
import sys
input = sys.stdin.readline

# 행 열
n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
    
direction = [(-1,0), (0,-1), (-1,-1)]

d = [[0 for _ in range(m)] for _ in range(n)]
for x in range(n):
    for y in range(m):
        d[x][y] = graph[x][y]
        for dx, dy in direction:
            xx = x+dx
            yy = y+dy
            if 0<=xx<n and 0<=yy<m:
                d[x][y] = max(graph[x][y]+d[xx][yy], d[x][y])
print(d[n-1][m-1])