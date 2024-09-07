# https://www.acmicpc.net/problem/2178
# 11시 8분
from sys import stdin
from collections import deque
n, m = map(int, stdin.readline().split())

miro = []
for _ in range(n):
    data = list(input())
    miro.append(list(map(int, data)))
    
# 상하좌우
direction = [(-1,0), (1,0), (0,-1), (0,1)]

def bfs(miro, queue):
    while queue:
        now_x, now_y = queue.popleft()
        
        for dx, dy in direction:
            x = now_x + dx
            y = now_y + dy
            # 미로를 벗어나면
            if x< 0 or y<0 or x>=n or y>=m:
                continue
            # 1이면
            if miro[x][y] == 1:
                # 이동 +1
                miro[x][y] = miro[now_x][now_y] + 1
                queue.append((x, y)) 

queue = deque([(0,0)])
bfs(miro, queue)
print(miro[n-1][m-1])