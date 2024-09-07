# https://www.acmicpc.net/problem/2606
# 7시 45분
computer = int(input())

connected = int(input())

graph =[[] for _ in range(computer+1)]

for _ in range(connected):
    node1, node2 = map(int, input().split())
    
    graph[node1].append(node2)
    graph[node2].append(node1)
    
 
# 1번 컴
def dfs(graph, node, visited):
    visited[node] = True
    
    for n in graph[node]:
        # 연결 되어 있고 안 들렸으면
        if visited[n] == False:
            dfs(graph, n, visited)
            
            

visited = [False] * (computer+1)
dfs(graph, 1, visited)
print(sum(visited)-1)