# 선행 작업 중 제일 늦게 끝나는 작업 + t

import sys
input = sys.stdin.readline
from collections import deque
n = int(input())

# 시간, 작업 수, 몇 번 작업
start = []
time = []
visited = [0] * (n+1)
graph = [[] for _ in range(n+1)] # 작업 후에 선행 작업을 저장하는 리스트
for i in range(1, n+1):
    t, k, *work = map(int, input().split())
    time.append(t)
    visited[i] = t
    if len(work) == 0:
        start.append(i)
    for w in work:
        graph[w].append(i)
    

# print(graph)

# 끝나는 시간을 저장하는
def dijkstra(nowork):
    q = deque(nowork)
    while q:
        v = q.popleft()
        for node in graph[v]:
            if visited[node] < visited[v] + time[node-1]:
                visited[node] = visited[v] + time[node-1]
                q.append(node)

dijkstra(start)

# print(visited)
print(max(visited))