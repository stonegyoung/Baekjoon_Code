import sys
input = sys.stdin.readline
n, t = map(int, input().split())
li = []
for _ in range(n):
    k, s = map(int, input().split())
    li.append((k,s))
    
graph = [[0]*(t+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, t+1):
        if li[i-1][0] > j:
            graph[i][j] = graph[i-1][j] # 선택안함. 그 위에 가치
        elif li[i-1][0] == j:
            graph[i][j] = max(li[i-1][1], graph[i-1][j]) # 선택 했을 때, 안했을 때
        else:
            w = j-li[i-1][0]
            graph[i][j] = max(li[i-1][1]+graph[i-1][w], graph[i-1][j]) # 선택+남은 시간 활용, 안했을 때
            
print(graph[n][t])