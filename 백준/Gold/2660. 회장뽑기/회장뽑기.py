# 9시 51분
import sys
input = sys.stdin.readline
INF = int(1e9)
# 회원 수
n = int(input())
graph = [[INF] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    graph[i][i] = 0
    
while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    graph[a][b] = 1
    graph[b][a] = 1
    
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][k] + graph[k][j], graph[i][j])

mini = []
for i in range(1, n+1):
    m = max([j for j in graph[i] if j!= INF])
    mini.append(m)
        
score = min(mini)
print(score, mini.count(score))
for i in range(len(mini)):
    if mini[i] == score:
        print(i+1, end=' ')