# 2 32
# 위상
import sys
from collections import deque
input = sys.stdin.readline

def ts(d0):
    q = deque(d0)
    res = []
    while q:
        v = q.popleft()
        res.append(v)
        for u in graph[v]:
            indegree[u] -= 1
            if indegree[u] == 0:
                q.append(u)
    return res

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
indegree = [0] * (N+1)
for _ in range(M):
    n, *lists = input().split()
    
    lists = list(map(int, lists))
    for i in range(int(n)-1):
        
        graph[lists[i]].append(lists[i+1])
        indegree[lists[i+1]] += 1
# print(graph)
# print(indegree)
d0 = []
for i in range(1, N+1):
    if indegree[i] == 0:
        d0.append(i)

result = ts(d0)
if len(result) == N:
    for r in result:
        print(r)
else:
    print(0)