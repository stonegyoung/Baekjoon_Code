# 6시 27분

# bfs로
import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

lists = [0]*100001
def bfs(start, target):
    queue = deque([start])
    lists[start] = 1
    
    while queue:
        v = queue.popleft()
        if v == target:
            return lists[v]
        for x in [2*v]:
            if 0<=x<100001:
                if lists[x] == 0:
                    lists[x] = lists[v]
                    queue.append(x)
        for x in [v-1, v+1]: # 위치
            if 0<=x<100001:
                if lists[x] == 0:
                    lists[x] = lists[v] + 1
                    queue.append(x)
        
                
if n > k:
    print(n-k)
elif n == k:
    print(0)
else:   
    print(bfs(n, k)-1) 