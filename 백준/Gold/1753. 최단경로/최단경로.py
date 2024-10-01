# 8시 20분
# 다익스트라

import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (distance[start], start))
    while q:
        cost, v = heapq.heappop(q)
        
        if cost > distance[v]:
            continue
        for i in graph[v]: # i[0]은 cost, i[1]은 노드
            c = cost + i[0]
            if c < distance[i[1]]:
                distance[i[1]] = c
                heapq.heappush(q, (c, i[1]))
                
V, e = map(int, input().split())
start = int(input())
graph = [[] for _ in range(V+1)]
distance = [INF for _ in range(V+1)]

for _ in range(e):
    # 방향
    u, v, w = map(int, input().split())
    graph[u].append((w, v)) # 가중치, 간선 
# print(graph)
    
dijkstra(start)
for i in distance[1:]:
    print(i if i != INF else 'INF')