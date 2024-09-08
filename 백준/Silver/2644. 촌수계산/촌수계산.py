# https://www.acmicpc.net/problem/2644
# 9시 35분
from sys import stdin
# 전체 수
n = int(stdin.readline().rstrip())
graph = [[] for _ in range(n+1)]
# 촌수 두 개
node1, node2 = map(int, stdin.readline().rstrip().split())
# m개의 관계
m = int(stdin.readline().rstrip())
for _ in range(m):
    n1, n2 = map(int, stdin.readline().rstrip().split())
    graph[n1].append(n2)
    graph[n2].append(n1)
    

cnt = 0
def dfs(graph, visited, now_node, target_node):
    for n in graph[now_node]:
        if n == target_node:
            visited[n] = visited[now_node]+1
            return True
        if visited[n] == 0: # 안 갔으면
            visited[n] = visited[now_node]+1
            dfs(graph, visited, n, target_node)

visited = [0]*(n+1)
visited[node1] = 1
res = dfs(graph, visited, node1, node2)
# 나중에 -1 해     
print(visited[node2]-1)