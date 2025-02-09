import sys
INF = int(1e9)
input = sys.stdin.readline
n = int(input()) # 교차로 수
graph = [[INF] *(n+1) for _ in range(n+1)]
for i in range(1, n):
    m = int(input())
    li = list(map(int, input().split()))
    for j in li:
        graph[i][j] = 1

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
# print(graph)
states = False
for i in range(1, n+1):
    if graph[i][i] != INF and graph[1][i]<INF: 
        states = True
        break
if states:
    print("CYCLE")
else:
    print("NO CYCLE")
