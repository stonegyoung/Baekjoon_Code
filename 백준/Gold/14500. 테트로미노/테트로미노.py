# 8시 52분
# 1+2+4+4+8
l1 = [
    [(0,1), (1,0), (1,1)],
    
    [(0,1), (0,2), (0,3)],
    [(1,0), (2,0), (3,0)],
    
    [(1,0), (1,1), (2,1)],
    [(0,1), (1,0), (1,-1)],
    [(1,0), (1,-1), (2,-1)],
    [(0,1), (1,1), (1,2)],
    
    [(0,1), (0,2), (1,1)],
    [(-1,1), (0,1), (1,1)],
    [(1,-1), (1,0), (1,1)],
    [(1,0), (1,1), (2,0)],
    
    [(1,0), (2,0), (2,1)],
    [(0,1), (0,2), (1,0)],
    [(0,1), (1,1), (2,1)],
    [(1,0), (1,-1), (1,-2)],
    [(1,0), (1,1), (1,2)],
    [(0,1), (0,2), (1,2)],
    [(0,1), (1,0), (2,0)],
    [(1,0), (2,0), (2,-1)],
]

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
    
def find_max(n, m, l1, graph):
    maxi = 0
    for i in range(n):
        for j in range(m):
            for l in l1:
                res = graph[i][j]
                for dx, dy in l:
                    x = i+dx
                    y = j+dy
                    if 0<=x<n and 0<=y<m:
                        res += graph[x][y]
                    else:
                        continue
                maxi = max(maxi, res)
    return maxi
                
result = find_max(n, m, l1, graph)
print(result)