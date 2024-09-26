# 2시 48분
import sys
sys.setrecursionlimit(10000000)
input = sys.stdin.readline

i=1
def dfs(V, E, R):
    global i
    V[R] = i
    i+=1
    for x in sorted(E[R]):
        if V[x] == 0:
            dfs(V,E,x)
            
n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    
    
visited = [0] * (n+1)
dfs(visited, graph, r)
for i in range(1, n+1):
    print(visited[i])