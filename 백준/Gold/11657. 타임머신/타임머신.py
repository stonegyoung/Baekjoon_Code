# 벨만포드
import sys
input = sys.stdin.readline
INF = int(1e9)

def bf(start, distance):
    distance[start] = 0
    # n번 반복(n-1 + 음수 순환을 보기 위한 1번)
    for i in range(n):
        for j in range(m): # 모든 간선 돈다
            cur, next, cost = edges[j]
            if distance[cur] != INF: # 무한대면 패스
                if distance[next] > distance[cur]+cost: # 짧으면 갱신
                    if i == n-1: # 마지막에 갱신되면 음수 간선 순환 존재
                        return True
                    distance[next] = distance[cur]+cost
    return False   

n, m = map(int, input().split())
edges = []
for _ in range(m):
    a,b,c = map(int, input().split())
    edges.append((a,b,c))
    
'''
1. 출발 노드 설정

2. 최단 거리 테이블 무한으로 초기화

3. 전체 간선을 돌면서 최단 거리 테이블 갱신 n번 반복
'''
start = 1
distance = [INF] * (n+1)                 
            
if bf(start, distance):
    print(-1)
else:
    for i in distance[2:]:
        print(i if i < INF else -1)