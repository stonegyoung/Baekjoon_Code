# 9시 49분
# 플워
import sys
input = sys.stdin.readline

n = int(input())
graph = [[0]*(n+1)]
for _ in range(n):
    lists = list(map(int, input().split()))
    graph.append([0] + lists)
    
# print(graph)
lines = set()

for i in range(1, n+1):
    for j in range(i+1, n+1):
        lines.add((i, j))
lenlines = len(lines)
# print(lines)

def fw():
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if i == j:
                    continue
                if i ==k or j == k:
                    continue
                if graph[i][j] == graph[i][k] + graph[k][j]:
                    if (i, j) in lines:
                        lines.remove((i,j))
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    return False
    return True
                    
if fw():
    total = 0
    for x, y in lines:
        total += graph[x][y]
    print(total)
else:
    print(-1)