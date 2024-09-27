# 9시 58분
import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)
directions = [(-1,0), (1,0), (0,-1), (0,1)]
    
def dijkstra(graph, visited, x,y):
    q = []
    heapq.heappush(q, (graph[x][y], x, y))
    visited[x][y] = graph[x][y]
    while q:
        cost, nowx, nowy = heapq.heappop(q)
        for dx, dy in directions:
            x = nowx + dx
            y = nowy + dy
            
            if 0<=x<n and 0<=y<n:
                if visited[x][y] < cost + graph[x][y]:
                    continue
                
                costs = cost + graph[x][y]
                if visited[x][y] > costs:
                    visited[x][y] = costs
                    heapq.heappush(q, (visited[x][y], x, y))
                
# bfs
cnt = 1
while True:
    n = int(input())
    
    if n == 0:
        break
    
    graph = []
    visited = [[INF]*n for _ in range(n)]
    for _ in range(n):
        graph.append(list(map(int, input().split())))
        
    dijkstra(graph, visited, 0, 0)
    # print(visited)
    print(f'Problem {cnt}: {visited[n-1][n-1]}')
    cnt+=1
        