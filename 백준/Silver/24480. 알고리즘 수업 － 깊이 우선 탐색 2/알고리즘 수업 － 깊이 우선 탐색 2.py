import sys
input = sys.stdin.readline

def dfs(start):
    cnt = 1
    st = [start]
    visited = [0] * (n+1)
    while st:
        node = st.pop()
        if visited[node] == 0:
            visited[node] = cnt
            cnt += 1
            st.extend(graph[node])
    for r in visited[1:]:
        print(r)    
    
n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    
for g in graph:
    g.sort()
    
dfs(r)
