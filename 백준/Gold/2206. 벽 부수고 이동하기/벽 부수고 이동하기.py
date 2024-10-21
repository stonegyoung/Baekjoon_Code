# 상태값을 큐에 같이 저장
import sys
input = sys.stdin.readline

from collections import deque

def bfs(startx, starty):
    q = deque([(startx, starty, 0)])
    visited[startx][starty][0]  = 1
    
    while q:
        nowx, nowy, state = q.popleft()
        if nowx==n-1 and nowy == m-1:
            return visited[nowx][nowy][state]
        for dx, dy in [(-1,0),(1,0),(0,1),(0,-1)]:
            x = nowx+dx
            y = nowy+dy
            if 0<=x<n and 0<=y<m:
                if visited[x][y][state] != 0: # 이미 방문 했으면
                    continue
                if graph[x][y] == 0: # 벽이 아니라면
                    visited[x][y][state] = visited[nowx][nowy][state] +1
                    q.append((x,y,state))
                else:    # 벽이면
                    if state == 1:
                        continue
                    # state == 0 이면
                    visited[x][y][1] = visited[nowx][nowy][state] +1
                    q.append((x,y,1))
    return -1

n, m = map(int, input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().rstrip())))

# print(graph)
# 벽을 부수기 전, 벽을 부수고 난 후
visited = [[[0,0] for _ in range(m)] for _ in range(n)]
# print(visited)

ans = bfs(0,0)
# print(visited)
print(ans)