# 상태값을 큐에 같이 저장
import sys
input = sys.stdin.readline

from collections import deque

def bfs(startx, starty):
    q = deque([(startx, starty, 0)])
    visited[startx][starty][0]  = 1
    
    while q:
        nowx, nowy, state = q.popleft()
        for dx, dy in [(-1,0),(1,0),(0,1),(0,-1)]:
            x = nowx+dx
            y = nowy+dy
            if 0<=x<n and 0<=y<m:
                # if visited[n-1][m-1][0] != 0 or visited[n-1][m-1][1] != 0:
                #     break
                if visited[x][y][state] != 0: # 이미 방문 했으면
                    continue
                if graph[x][y] == 0:
                    visited[x][y][state] = visited[nowx][nowy][state] +1
                    q.append((x,y,state))
                else:    
                    if state == 1:
                        continue
                    visited[x][y][state+1] = visited[nowx][nowy][state] +1
                    q.append((x,y,state+1))

n, m = map(int, input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().rstrip())))

# print(graph)
# 벽을 부수기 전, 벽을 부수고 난 후
visited = [[[0,0] for _ in range(m)] for _ in range(n)]
# print(visited)

bfs(0,0)
state0 = visited[n-1][m-1][0]
state1 = visited[n-1][m-1][1]
if state0==0 and state1 == 0:
    print(-1)
elif state0 == 0:
    print(state1)
elif state1 == 0:
    print(state0)
else:
    print(min(state0, state1))