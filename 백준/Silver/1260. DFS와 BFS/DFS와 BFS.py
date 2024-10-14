# https://www.acmicpc.net/problem/1260
# 6시 50분
from collections import deque
def dfs(start_node, graph, d_visited):
    d_visited[start_node] = True
    print(start_node, end=' ')
    for node in graph[start_node]:
        if d_visited[node] == False:
            dfs(node, graph, d_visited)
        

def bfs(start_node, graph, b_visited):
    queue = deque([start_node])
    b_visited[start_node] = True
    while queue:
        v = queue.popleft()
       
        print(v, end=' ')
        for node in graph[v]:
            if b_visited[node] == False:
                queue.append(node)
                b_visited[node] = True
 



n, m, v = (map(int, input().split()))
graph = [ [] for _ in range(n+1)]

for _ in range(m):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)
    
for g in graph:
    g.sort()
    
d_visited = [ False for _ in range(n+1)]
b_visited = [ False for _ in range(n+1)]

dfs(v, graph, d_visited)
print()
bfs(v, graph, b_visited)
    

