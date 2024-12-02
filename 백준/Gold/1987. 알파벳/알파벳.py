# 2:26
# dfs
import sys
input = sys.stdin.readline
cnt = 1
def dfs(startx, starty, visited, no):
    global cnt
    cnt = max(cnt, no)
    for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
        x = startx+dx
        y = starty+dy
        if 0<=x<r and 0<=y<c and graph[x][y] not in visited:
            xy = graph[x][y]
            visited.add(xy)
            dfs(x, y, visited, no+1)
            visited.remove(xy)
    
r, c = map(int, input().split())
graph = []
for _ in range(r):
    graph.append(list(input().rstrip()))
    
# print(graph)
visited = set(graph[0][0])
dfs(0,0, visited, 1)
print(cnt)