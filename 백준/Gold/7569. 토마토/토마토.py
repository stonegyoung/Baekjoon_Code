# 11시 3분
from sys import stdin
from collections import deque
# 열 행
m, n, h = map(int, stdin.readline().rstrip().split())

lists = []
for _ in range(h):
    data = []
    for i in range(n):
        tomatos = list(map(int, stdin.readline().rstrip().split()))
        data.append(tomatos)
    lists.append(data)
    
direction = [(0, -1, 0),(0, 1, 0),(0, 0, -1),(0, 0, 1),(-1, 0, 0),(1,0,0)]

def bfs(is_1):
    queue = deque(is_1)
    while queue:
        now_h,now_n,now_m = queue.popleft()
        for dh, dn, dm in direction:
            l = now_h + dh
            x = now_n + dn
            y = now_m + dm
            # 범위 안에 있고
            if 0<=l<h and 0<=x<n and 0<=y<m:
                # 안 익었으면
                if lists[l][x][y] == 0:
                    queue.append((l,x,y))
                    lists[l][x][y] = lists[now_h][now_n][now_m] +1
                # 익었는데 좀 더 빨리 익은 날짜면
                else:
                    if lists[l][x][y] > lists[now_h][now_n][now_m] +1:
                        lists[1][x][y] = lists[now_h][now_n][now_m] +1
is_1 = []        
for i in range(h):
    for j in range(n):
        for k in range(m):
            if lists[i][j][k] == 1: # 익은 거 있을 때만
                is_1.append((i,j,k))

bfs(is_1)

maxi = -1
mini = 100000
for i in range(h):
    for j in range(n):
        for k in range(m):
            if lists[i][j][k] == 0:
                mini = -1
                break
            if maxi < lists[i][j][k]:
                maxi = lists[i][j][k]
            
# 다 하루씩 빼야 함
print(maxi-1 if mini == 100000 else mini)