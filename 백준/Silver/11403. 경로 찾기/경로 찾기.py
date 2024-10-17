# 1시 18분
# 플로이드

import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, (input().split()))))
    
# print(graph)

for i in range(n):
    for j in range(n):
        if graph[i][j] == 0:
            graph[i][j] = INF
# print(graph)

for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                continue
            if graph[i][k] + graph[k][j] < INF:
                graph[i][j] = 1

for i in range(n):
    for j in range(n):
        print(graph[i][j] if graph[i][j] != INF else 0, end=' ')
    print()
