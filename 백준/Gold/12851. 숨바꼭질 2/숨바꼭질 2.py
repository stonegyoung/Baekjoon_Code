# 9시 28분
# bfs
import sys
from collections import deque
input = sys.stdin.readline

def bfs(start, end):
    visited[start] = 0
    queue = deque([start])
    cnt[start]=1
    while queue:
        v = queue.popleft()
        for x in [v*2, v-1, v+1]:
            if 0 <= x < 100001:
                if visited[x] == -1:
                    visited[x] = visited[v]+1
                    cnt[x] += cnt[v]
                    queue.append(x)
                else:
                    if visited[v]+1 == visited[x] and visited[v] != -1: # 같으면
                        cnt[x] += cnt[v]
                    elif visited[v]+1 < visited[x] and visited[v] != -1:
                        cnt[x] = 1
                    
n, m = map(int, input().split())
if n >= m:
    print(n-m)
    print(1)
else:
    visited = [-1] * (100001)
    cnt = [0] * (100001)
    bfs(n, m)
    print(visited[m])
    print(cnt[m])