from sys import stdin
from collections import deque

# 총 수, 지금 위치, 기업 위치, 올라가는 수, 내려가는 수
F, S, G, U, D = map(int, stdin.readline().split())

stairs = G

d = [1000001] * (F+1)
d[S] = 0

def bfs(start):
    queue = deque([start])
    
    while queue:
        v = queue.popleft()
        if D == 0:
            pass
        else:
            if v-D > 0:
                if d[v-D] == 1000001:# 들렸으면
                    d[v-D] = d[v]+1
                    queue.append(v-D)
                else: # 안들렸으면
                    # 비교
                    d[v-D] = min(d[v-D], d[v]+1)
        if U == 0:
            pass
        else:
            if v+U <= F:
                if d[v+U] == 1000001:# 들렸으면
                    d[v+U] = d[v]+1
                    queue.append(v+U)
                else: # 안들렸으면
                    # 비교
                    d[v+U] = min(d[v-D], d[v]+1)
    
bfs(S)
# print(d) 
print(d[stairs] if d[stairs]!=1000001 else 'use the stairs')