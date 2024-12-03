#12:27
# 위상 정렬
import sys
from collections import deque
input = sys.stdin.readline

def bfs(d0, graph, time, indegree):
    q = deque(d0)
    while q:
        node, t = q.popleft()
        for v in graph[node]:
            indegree[v] -= 1
            visited[v] = max(visited[v], t+time[v])
            if indegree[v] == 0:
                q.append((v, visited[v]))
                # print(visited)

n = int(input())
# 시간 번호 -1
graph = [[] for _ in range(n+1)]
indegree = [0]*(n+1)
visited = [0] * (n+1)
time = [0] * (n+1)
d0 = []
for i in range(1, n+1):
    t, *num = map(int, input().split())
    for n in num[:-1]:
        graph[n].append(i)
    time[i] = t
    indegree[i] = len(num[:-1])
    
    if indegree[i] == 0:
        visited[i] = t
        d0.append((i, t))

bfs(d0, graph, time, indegree)
for v in visited[1:]:
    print(v)