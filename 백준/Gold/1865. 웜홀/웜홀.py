# 1시 7분
# 벨만
import sys
input = sys.stdin.readline
INF = int(1e9)
def bf(start, dist):
    dist[start] = 0
    for i in range(n):
        for node, cost in edges.items():
            now, nextn = node
            if dist[nextn] > dist[now]+cost:
                if i == n-1:
                    return True
                dist[nextn] = dist[now]+cost
                
    return False
                        
            
            

tc = int(input())

for _ in range(tc):
    n, m, w = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    edges = {}
    for _ in range(m):
        S, E, T = map(int, input().split())
        if edges.get((S,E), T) >= T:
            edges[(S,E)] = T
        if edges.get((E,S), T) >= T:
            edges[(E,S)] = T
    for _ in range(w):
        S, E, T = map(int, input().split())
        if edges.get((S,E), T) >= -T:
            edges[(S,E)] = -T
    distance = [INF] * (n+1)
    if bf(0, distance):
        print("YES")
    else:
        # print(distance)
        print("NO")
    # print(edges)