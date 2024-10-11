# 2시 28분
# 다익스트라

import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start, end):
    q = []
    distance[start] = 0
    city[start] = [start]
    heapq.heappush(q, (0, start))
    
    while q:
        c, node = heapq.heappop(q)
        
        if c > distance[node]:
            continue
        
        for i in graph[node]: # i[0] distance i[1] node
            cost = c + i[0]
            if cost < distance[i[1]]:
                distance[i[1]] = cost
                city[i[1]] = city[node] + [i[1]]
                heapq.heappush(q, (cost, i[1]))
                
    print(distance[end])
    a = city[end]
    print(len(a))
    for i in a:
        print(i, end=' ')
        

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    
distance = [INF] * (n+1)
city = {}

start, end = map(int, input().split())
dijkstra(start, end)

