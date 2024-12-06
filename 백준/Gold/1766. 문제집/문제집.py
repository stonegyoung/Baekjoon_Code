# 10:17
# 위상
import sys
import heapq
input = sys.stdin.readline

def ts(starts):
    stack = starts
    heapq.heapify(stack)
    visited = []
    while stack:
        now = heapq.heappop(stack)
        visited.append(now)
        r = []
        for v in graph[now]:
            indegree[v] -= 1
            if indegree[v] == 0:
                heapq.heappush(stack, v)
        # stack.extend(sorted(r, reverse=True))
    return visited

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1) 
for _ in range(m):
    a, b = map(int, input().split())
    indegree[b] += 1
    graph[a].append(b)
    
i0 = [i for i in range(1, n+1) if indegree[i] == 0]

visit = ts(i0)
# for v in visit:
#     print(v, end=' ')
print(*visit)