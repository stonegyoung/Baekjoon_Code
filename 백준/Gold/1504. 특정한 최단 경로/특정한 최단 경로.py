# 12시 44분
# 플워 -> 다익
import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start, end, graph, distance):
    q = []
    heapq.heappush(q, (0, start))
    
    while q:
        cost, node = heapq.heappop(q)
        
        if cost > distance[node]:
            continue
        for i in graph[node]: # i[0]은 cost, i[1]은 노드
            c = cost + i[0]
            if c < distance[i[1]]:
                distance[i[1]] = c
                heapq.heappush(q, (c, i[1]))
    return distance[end] 

n, e = map(int, input().split())
g =  [[] for _ in range(n+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    g[a].append((c, b))
    g[b].append((c, a))
    
v1, v2 = map(int, input().split())

def min_distance(s, e):
    if s == e:
        return 0
    distance = [INF] * (n+1)
    return dijkstra(s, e, g, distance)

tov1 = min_distance(1, v1)
v1tov2 = min_distance(v1, v2)
v2ton = min_distance(v2, n)
tov2 = min_distance(1, v2)
v2tov1 = min_distance(v2, v1)
v1ton = min_distance(v1, n)

res = min(
        (tov1 + v1tov2 + v2ton), # 1 -> v1 -> v2 -> n
        (tov2 + v2tov1 + v1ton), # 1 -> v2 -> v1 -> n
        (tov1 +v1tov2 + v2tov1 + v1ton), # 1 -> v1 -> v2 -> v1 -> n
        (tov2 + v2tov1 + v1tov2 + v2ton) # 1 -> v2 -> v1 -> v2 -> n
    )
if res >= INF:
    print(-1)
else:
    print(res)