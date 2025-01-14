import sys
sys.setrecursionlimit(10**6)  # 재귀 깊이 제한 설정
input = sys.stdin.readline

# 입력 받기
N, M, R = map(int, input().split())

# 그래프 초기화 (인접 리스트)
graph = [[] for _ in range(N + 1)]

# 간선 입력 받기
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 오름차순 방문을 위해 정렬
for adj in graph:
    adj.sort()

# 각 노드의 깊이를 -1로 초기화
depth = [-1] * (N + 1)

# DFS 함수
def dfs(node, d):
    depth[node] = d  # 현재 노드의 깊이 기록
    for neighbor in graph[node]:
        if depth[neighbor] == -1:  # 방문하지 않았다면
            dfs(neighbor, d + 1)

# DFS 실행 (시작 노드, 깊이 0부터 시작)
dfs(R, 0)

# 결과 출력
for d in depth[1:]:
    print(d)
