# 9시 31분
import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

# 도시 수
n = int(input())
# 버스 수
m = int(input())
graph =[[] for _ in range(n+1)]
for _ in range(m):
    # 출발 도착 비용
    a, b, c = map(int, input().split())
    \
    # 단방향
    graph[a].append((c, b)) # 비용, 도착
    

# 출발, 도착
start, target = map(int, input().split())
distance = [INF] * (n+1)
# print(graph)

def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    
    while q:
        dist, v = heapq.heappop(q)
        
        if distance[v] < dist:
            continue
        
        for i in graph[v]: # i[0]은 cost, i[1]은 노드
            cost = distance[v] + i[0]
            
            if cost < distance[i[1]]:
                distance[i[1]] = cost
                heapq.heappush(q, (distance[i[1]], i[1]))
                
dijkstra(start)
# print(distance)
print(distance[target])