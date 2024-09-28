# 4시 20분
# 누적합
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
sum_graph = [[0]*(n+1)]
for _ in range(n):
    lists = (list(map(int, input().split())))
    sumlists = [0] * (n+1)
    for i in range(1, n+1):
        sumlists[i] = sumlists[i-1] + lists[i-1]
    sum_graph.append(sumlists)
    
# print(sum_graph)

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    
    summ = 0
    # x1행부터x2행까지
    for x in range(x1, x2+1):
        # y1열~y2열까지
        summ += sum_graph[x][y2] - sum_graph[x][y1-1]
    print(summ)