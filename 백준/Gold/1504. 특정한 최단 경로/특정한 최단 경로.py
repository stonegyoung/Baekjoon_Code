import sys
input = sys.stdin.readline
INF = int(1e9)

def fw(graph):
    for k in range(1, n+1):
        gk = graph[k]
        for i in range(1, n+1):
            gi = graph[i]
            for j in range(1, n+1):
                if i == j:
                    continue
                gi[j] = min(gi[k]+gk[j], gi[j])

n, e = map(int, input().split())


graph = [[INF]*(n+1) for _ in range(n+1)]
for i in range(1, n+1):
    graph[i][i] = 0
    
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a][b] = c
    graph[b][a] = c

fw(graph)

v1, v2 = map(int, input().split())
res = min(graph[1][v1] + graph[v1][v2] + graph[v2][n], 
          graph[1][v2] + graph[v2][v1] + graph[v1][n],
          graph[1][v1] + graph[v1][v2] + graph[v2][v1] + graph[v1][n],
          graph[1][v2] + graph[v2][v1] + graph[v1][v2] + graph[v2][n]          
        )
if res >= INF :
    print(-1)
else:
    print(res)