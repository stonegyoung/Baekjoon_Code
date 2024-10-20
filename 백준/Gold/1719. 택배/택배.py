# 1시 55분
import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start, distance, n):
    parent = ['-'] * (n+1)
    q = []
    
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q:
        c, n = heapq.heappop(q)
        
        if c > distance[n]:
            continue
        for i in graph[n]: # i[0] cost i[1] node
            cost = c + i[0]
            if cost < distance[i[1]]:
                if n == start:
                    parent[i[1]] = str(i[1])
                else:
                    parent[i[1]] = str(parent[n])
                distance[i[1]] = cost
                heapq.heappush(q, (cost, i[1]))
    return parent[1:]

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((c,b))
    graph[b].append((c,a))
    
# print(graph)

for i in range(1, n+1):
    distance = [INF] * (n+1)
    r = dijkstra(i, distance, n)
    print(' '.join(r))
    # print(distance)
    