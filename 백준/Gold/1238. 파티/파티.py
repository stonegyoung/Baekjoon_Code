# 9시 51분
# 다익
import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
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
graph = [[] for _ in range(n+1)]

for _ in range(m):
    s, e, t = map(int, input().split())
    graph[s].append((t,e)) # time, node
    
# print(graph)
dd = []
for i in range(1,n+1):
    distance = [INF for _ in range(n+1)]
    dijkstra(i)
    dd.append(distance)
    
res = [0] + [i for i in dd[x-1][1:]]
for i in range(1, n+1):
    if i == x:
        pass
    res[i] += dd[i-1][x]
    
print(max(res))