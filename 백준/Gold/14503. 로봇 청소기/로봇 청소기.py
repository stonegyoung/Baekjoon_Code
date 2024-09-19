# 11시 18분~55
# 3시 44분~ 4시 48분
#   북
# 서   동
#   남
# 현재 칸 청소
# 다 청소 됐으면 한 칸 후진(벽이면 멈춤)
# 청소되지 않은 칸이 있으면 반시계 회전
# 앞이 청소되지 않았으면 전지
import sys
from collections import deque
input = sys.stdin.readline
# 행 열
n, m = map(int, input().split())
r, c, d = map(int, input().split()) # 0북 1동 2남 3서

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
    
# 북동남서 -1씩 빼
w = [(-1, 0), (0, 1), (1, 0), (0, -1)]
def dfs(nowx, nowy,d):
    cnt = 0
    queue = deque([(nowx, nowy)])
    
    while queue:
        
        nowx, nowy = queue.popleft()
        # 현재 칸 청소
        if graph[nowx][nowy] == 0:
            graph[nowx][nowy] = 0.5
            cnt += 1
            
        if check(nowx, nowy): # 청소 되지 않은 게 있으면
            # 반시계 방향으로 회전
            while True:
                d = d-1 if d>0 else 3
                if graph[nowx+w[d][0]][nowy+w[d][1]] ==0:
                    queue.append((nowx+w[d][0], nowy+w[d][1]))
                    break
        else:
            # 청소 됐거나 벽이면
            if graph[nowx-w[d][0]][nowy-w[d][1]] == 1:
                break # 벽이면 멈춰
            else: # 벽 아니면 후진
                x = nowx - w[d][0]
                y = nowy - w[d][1]
                queue.append((x,y))
    return cnt
            
# 앞 뒤 좌 우 보는 코드
def check(nowx, nowy):
    for dx, dy in w:
        x = nowx + dx
        y = nowy + dy
        if 0<=x<n and 0<=y<m:
            if graph[x][y] == 0:
                return True
    return False

print(dfs(r,c,d))