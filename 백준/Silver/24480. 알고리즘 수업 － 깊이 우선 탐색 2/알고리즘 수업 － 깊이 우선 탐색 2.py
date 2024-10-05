# 3시 12분
# dfs
import sys
input = sys.stdin.readline

# cnt = 1
def dfs(start, graph, visited):
    cnt = 1
    stack = [start]
    while stack:
        node = stack.pop()
        if visited[node]: # 이미 방문했으면 패스
            continue
        visited[node] = cnt
        cnt += 1
        for n in graph[node]:
            if visited[n] == 0:
                stack.append(n)

n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    
for g in graph:
    g.sort()
dfs(r, graph, visited)
for v in visited[1:]:
    print(v)