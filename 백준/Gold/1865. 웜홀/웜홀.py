import sys
inf = 10001
input = sys.stdin.readline

tc = int(input())

def bellman_ford(start):
    dist[start] = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            for nxt, time in graph[j]:
                if dist[nxt] > dist[j] + time:
                    dist[nxt] = dist[j] + time
                    if i == n:
                        return True
    return False


for _ in range(tc):
    n, m, w = map(int, input().split())
    graph = [[] for i in range(n+1)]
    dist = [inf for i in range(n+1)]
    for i in range(m):
        s, e, t = map(int, input().split())
        graph[s].append([e, t])
        graph[e].append([s, t])
    for i in range(w):
        s, e, t = map(int, input().split())
        graph[s].append([e, -t])

    if bellman_ford(1):
        print("YES")
    else:
        print("NO")