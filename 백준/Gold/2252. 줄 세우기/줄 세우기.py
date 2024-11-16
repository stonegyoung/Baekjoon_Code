# 11 33
# 위상
import sys
input = sys.stdin.readline
from collections import deque

def ts(queue):
    q = deque(queue)
    while q:
        v = q.popleft()
        print(v, end = ' ')
        for node in graph[v]:
            indegree[node] -= 1

            if indegree[node] == 0:
                q.append(node)

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
indegree = [0]* (n+1)
for _ in range(m):
    A, B = map(int, input().split())
    graph[A].append(B) # 단방향
    indegree[B] += 1

queue = []
for i in range(1, n+1):
    if indegree[i] == 0:
        queue.append(i)
ts(queue)