# 1시 7분
# 벨만
import sys
input = sys.stdin.readline
INF = int(1e9)
def bf(start, dist):
    for s in start:
        dist[s] = 0
        for i in range(n):
            for now in range(1, n+1):
                for nextn, cost in edges[now]:
                    if dist[now] != INF:
                        if dist[nextn] > dist[now]+cost:
                            if i == n-1:
                                return True
                            dist[nextn] = dist[now]+cost
                        
    return False

            

tc = int(input())

for _ in range(tc):
    start = []
    n, m, w = map(int, input().split())
    edges = [[]*(n+1) for _ in range(n+1)]
    for _ in range(m):
        S, E, T = map(int, input().split())
        edges[S].append((E,T))
        edges[E].append((S,T))
    for _ in range(w):
        S, E, T = map(int, input().split())
        edges[S].append((E,-T))
        start.append(S)
    distance = [INF] * (n+1)
    if bf(start, distance):
        print("YES")
    else:
        # print(distance)
        print("NO")
    # print(edges)
