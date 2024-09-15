from sys import stdin
from collections import deque
n = int(stdin.readline())

def minus(arr, height):
    data = []
    for a in arr:
        data.append(list(map(lambda x: x-height if x>height else 0, a)))
    return data

def bfs(graph, i, j):
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([(i, j)])
    graph[i][j] = 0
    
    while queue:
        now_x, now_y = queue.popleft()
        for dx, dy in direction:
            x = now_x + dx
            y = now_y + dy
            if 0<=x<n and 0<=y<n:
                if graph[x][y] > 0 :
                    queue.append((x,y))
                    graph[x][y] = 0
        
graph = []
maxi = 0
for _ in range(n):
    lists = list(map(int, stdin.readline().split()))
    maxi = max(max(lists), maxi)
    graph.append(lists)

# 1부터 max 값 -1까지 res 저장
result = []
for height in range(0,maxi):
    data = minus(graph, height)
    res = 0
    for i in range(n):
        for j in range(n):
            if data[i][j] > 0:
                bfs(data, i, j)
                res += 1
    result.append(res)
                
# print(result)
print(max(result))