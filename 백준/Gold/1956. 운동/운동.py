# 2시 1분
# 플로이드
import sys
input = sys.stdin.readline
INF = int(1e9)

v, e = map(int, input().split())

graph = [[INF]*(v+1) for _ in range(v+1)]
    
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a][b] = c # 단방향
    
for k in range(1, v+1):
    for i in range(1, v+1):
        for j in range(1, v+1):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])
 
mini = INF
for i in range(1, v+1):
    if graph[i][i] != INF:
        mini = min(mini, graph[i][i])
        
print(mini if mini != INF else -1)