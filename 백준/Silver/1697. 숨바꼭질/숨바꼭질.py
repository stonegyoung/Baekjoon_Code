from sys import stdin
from collections import deque

# 수빈, 동생
n, k = map(int, stdin.readline().split())

visited = [0] * 100001

def find_syster(n, k):
    queue = deque([n])
    
    while queue:
        v = queue.popleft()
        if v == k:
            return visited[k]
        
        for x in [v+1, 2*v, v-1]:
            if 0 <= x < len(visited):
                if visited[x]==0:    
                    visited[x] = visited[v]+1
                    queue.append(x)
                elif visited[x] > visited[v]+1:
                    visited[x] = visited[v]+1
                    
                    
print(find_syster(n,k))