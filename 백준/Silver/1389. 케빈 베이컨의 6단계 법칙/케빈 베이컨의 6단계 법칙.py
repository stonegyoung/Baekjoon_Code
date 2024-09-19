# 10시 48분
import sys
input = sys.stdin.readline

INF = int(1e9)

# 유저 수, 친구 수
n, m = map(int, input().split())
graph = [[INF]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    
    # 양방향
    graph[a][b] = 1
    graph[b][a] = 1
# print(graph)


# 자기 자신 초기화
for i in range(1, n+1):
    graph[i][i] = 0
    
# 점화식
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])
            
max_idx = 1
for i in range(2, n+1):
    total = sum(graph[i])
    if total < sum(graph[max_idx]):
        max_idx = i

print(max_idx)