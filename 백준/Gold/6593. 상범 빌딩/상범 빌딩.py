# 7시 52분

import sys
from collections import deque
input = sys.stdin.readline
INF = int(1e9)
directions = [(0,0,1), (0,0,-1), (0,1,0), (0,-1,0), (-1,0,0), (1,0,0)]
def bfs(visited, start):
    s1, s2, s3 = start
    queue = deque([(s1,s2,s3)])
    visited[s1][s2][s3] = 0
    while queue:
        nowl, nowr, nowc = queue.popleft()
        for dl, dr, dc in directions:
            ll = nowl + dl
            rr = nowr + dr
            cc = nowc + dc
            if 0<=ll<l and 0<=rr<r and 0<=cc<c:
                if graph[ll][rr][cc] == '.' or graph[ll][rr][cc] == 'E':
                    if visited[nowl][nowr][nowc] + 1 < visited[ll][rr][cc]:
                        visited[ll][rr][cc] = visited[nowl][nowr][nowc] + 1
                        queue.append((ll,rr,cc))
                
                      
while True:
    l, r, c = map(int, input().split())
    
    if l==0 and r==0 and c==0:
        break
    
    graph = []
    for _ in range(l):
        d = []
        for _ in range(r):
            d.append(list(input().rstrip()))
        input()
        graph.append(d)
        
    
    Start, End = [], []
    for i in range(l):
        for j in range(r):
            for k in range(c):
                if graph[i][j][k] == 'S':
                    Start = [i,j,k]
                if graph[i][j][k] =='E':
                    End =[i,j,k]
                    
    visited = [[[INF] * c for _ in range(r)] for _ in range(l)]
    
    bfs(visited, Start)
    res = visited[End[0]][End[1]][End[2]]
    if res == INF:
        print('Trapped!')
    else:
        print(f'Escaped in {res} minute(s).')