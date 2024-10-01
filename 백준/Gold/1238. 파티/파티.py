# 9시 51분~10시 11분
# 다익
import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start, distance, graph):
    q = []
    distance[start] = 0
    heapq.heappush(q, (distance[start], start))
    
    while q:
        time, v = heapq.heappop(q)
        if time > distance[v]:
            continue
        for i in graph[v]: # i[0] time i[1] node
            cost = time + i[0]
            if cost < distance[i[1]]:
                distance[i[1]] = cost
                heapq.heappush(q, (cost, i[1]))
    

n, m, x = map(int, input().split())

# x번으로 갔다가 오기
come = [[] for _ in range(n+1)]
go = [[] for _ in range(n+1)]
come_distance = [INF] *(n+1)
go_distance = [INF] *(n+1)

for _ in range(m):
    s, e, t = map(int, input().split())
    come[s].append((t,e)) # time, node
    go[e].append((t,s))
    
# print(come)
dijkstra(x, come_distance, come)
dijkstra(x, go_distance, go)

maxi = -1
for i in range(1, n+1):
    maxi = max(maxi, come_distance[i]+go_distance[i])
print(maxi)