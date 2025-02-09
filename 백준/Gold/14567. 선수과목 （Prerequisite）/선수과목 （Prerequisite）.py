import sys
from collections import deque
input = sys.stdin.readline

def ts(degree, graph):
    sm = [1 for _ in range(len(degree))]
    degree0 = [i for i in range(1, len(degree)) if degree[i] == 0]

    q = deque(degree0)
    while q:
        now = q.popleft()
        for v in graph[now]:
            sm[v] = sm[now] + 1
            degree[v] -= 1
            if degree[v] == 0:
                q.append(v)
    for i in (sm[1:]):
        print(i, end=' ')

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
degree = [0] * (n+1)
for _ in range(m):
    first, second = map(int, input().split())
    graph[first].append(second)
    degree[second] += 1
    
ts(degree, graph)