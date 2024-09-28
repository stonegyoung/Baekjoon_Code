# https://www.acmicpc.net/problem/16953
# 1tl 13
#dp /bfs/dijkstra

import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    distance[start] = 1
    q = []
    heapq.heappush(q, (distance[start], start))
    
    while q:
        cost, v = heapq.heappop(q)
        if cost > distance[v]:
            continue
        if v*2 > b and int(str(v)+'1') > b:
            continue
        for node in [v*2, int(str(v)+'1')]:
            if node <= b:
                if node in distance:
                    if distance[node] > cost + 1:
                        distance[node] = cost + 1
                        if node == b:
                            return distance[node]
                        heapq.heappush(q, (distance[node], node))
                else:
                    distance[node] = cost+1
                    if node == b:
                        return distance[node]
                    heapq.heappush(q, (distance[node], node))
    return -1

a, b = map(int, input().split())

if a==b:
    print(1)
elif a>b:
    print(-1)
else:
    distance = {}
    print(dijkstra(a))
