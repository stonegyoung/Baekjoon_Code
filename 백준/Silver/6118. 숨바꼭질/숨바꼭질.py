# 11시 35분
# 다익스트라: 한 곳에서 다른 한 쪽까지
# max인 것 똑같으면 가장 작은 것
import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
start = 1
dist = [INF] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    # 양방향
    graph[a].append(b) 
    graph[b].append(a) 
    
def dijkstra(start):
    q = []
    dist[start] = 0
    heapq.heappush(q, (dist[start] ,start))
    
    while q:
        d, v = heapq.heappop(q)
        if dist[v] < d:
            continue
        for node in graph[v]: # 0은 거리 1은 노드
            cost = d + 1
            if cost < dist[node]:
                dist[node] = cost
                heapq.heappush(q, (dist[node], node))
                
dijkstra(start)
maxi = 0
idx = 0
for i, d in enumerate(dist):
    if d == INF:
        pass
    else:
        if d > maxi:
            maxi = d
            idx = i
        
print(idx, dist[idx], dist.count(dist[idx]))
        