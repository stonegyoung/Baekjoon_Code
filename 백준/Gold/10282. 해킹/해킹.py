import sys
import heapq
INF = int(1e9)
input = sys.stdin.readline

def dijkstra(c):
    q = []
    distance[c] = 0
    heapq.heappush(q, (0,c))
    
    while q:
        cost, node = heapq.heappop(q)
        
        if cost > distance[node]:
            continue
        for v in graph[node]: # v[0] cost v[1] node 
            dist = cost + v[0]
            if dist < distance[v[1]]:
                distance[v[1]] = dist
                heapq.heappush(q, (dist, v[1]))
     

t = int(input())

for _ in range(t):
    n, d, c = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    distance = [INF] * (n+1)
    for _ in range(d):
        a, b, s = map(int, input().split())
        graph[b].append((s,a)) # 초, 의존

    # print(graph)
    
    dijkstra(c)
    total = 0
    maxi = 0
    for d in distance[1:]:
        if d != INF:
            # print(d)
            total += 1
            maxi = max(maxi, d)
    print(total, maxi)