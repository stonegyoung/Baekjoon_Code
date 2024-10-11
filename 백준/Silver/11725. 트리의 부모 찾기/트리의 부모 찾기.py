# 1시 54분 
import sys
input= sys.stdin.readline
from collections import deque

n = int(input())


parents = [i for i in range(n+1)]
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)
    
visited = [False] * (n+1)
def dfs(node):
    st = [node]
    
    while st:
        v = st.pop()
        for n in graph[v]:
            if visited[n] == False:
                parents[n] = v
                visited[n] = True
                st.append(n)
dfs(1)
for i in parents[2:]:
    print(i)
    
    