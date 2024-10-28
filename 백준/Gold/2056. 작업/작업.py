# 위상 정렬
# https://m.blog.naver.com/ndb796/221236874984

import sys
input = sys.stdin.readline
from collections import deque
n = int(input())

# 시간, 작업 수, 몇 번 작업
q = deque()
indegree = [0] * (n+1)
time = []
visited = [0] * (n+1)
graph = [[] for _ in range(n+1)] # 작업 후에 선행 작업을 저장하는 리스트
for i in range(1, n+1):
    t, k, *work = map(int, input().split())
    time.append(t)
    if len(work) == 0:
        q.append(i) # 0인 작업 추가
        visited[i] = t # 0이면 자기 시간만 추가
    for w in work:
        graph[w].append(i)
        indegree[i] += 1 # 진입 차수 추가

# print(graph)

# 끝나는 시간을 저장하는
def bfs():
    # 진입 차수가 0인 것만 append
    while q:
        v = q.popleft()
        for node in graph[v]:
            visited[node] = max(visited[node], visited[v] + time[node-1])
            indegree[node] -= 1
            if indegree[node] == 0:
                q.append(node)

bfs()
# print(indegree)
# print(graph)
# print(visited)
print(max(visited))