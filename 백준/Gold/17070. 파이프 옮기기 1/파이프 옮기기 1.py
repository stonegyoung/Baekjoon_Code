# # dfs/bfs
# # 상태값도 0 가로 1 세로 2 대각선
# import sys
# from collections import deque
# input = sys.stdin.readline

# def go0(nowx, nowy, q):
#     x = nowx
#     y = nowy+1
#     if 0<=x<n and 0<=y<n:
#         if graph[x][y] == 0 :
#             q.append((x,y,0))
        
# def go1(nowx, nowy, q):
#     x = nowx+1
#     y = nowy
#     if 0<=x<n and 0<=y<n:
#         if graph[x][y] == 0 :
#             q.append((x,y,1))
        
# def go2(nowx, nowy, q):
#     x = nowx+1
#     y = nowy+1
#     if 0<=x<n and 0<=y<n:
#         if graph[nowx+1][nowy] == 0 and graph[nowx][nowy+1] == 0 and graph[x][y] == 0:
#             q.append((x,y,2))
                
# def dfs(start):
#     q = deque([start])
#     cnt = 0
#     while q:
#         nowx, nowy, state = q.pop()
#         if nowx == n-1 and nowy==n-1:
#             cnt += 1
#             continue
#         if state == 0: # 가로
#             go0(nowx, nowy, q)
#             go2(nowx, nowy, q)
#         elif state == 1: # 세로
#             go1(nowx, nowy, q)
#             go2(nowx, nowy, q) 
#         else: # 대각선
#             go0(nowx, nowy, q)
#             go1(nowx, nowy, q)
#             go2(nowx, nowy, q)
#     return cnt

# n = int(input())
# graph = []
# for _ in range(n):
#     graph.append(list(map(int, input().split())))
    

# cnt = dfs((0,1,0))
# print(cnt)


# dp
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
    
dp = [[[0, 0, 0] for _ in range(n)] for _ in range(n)] # 현재 칸을 끝으로 하는 가로, 세로, 대각선 파이프 수
# print(dp)
dp[0][1][0] = 1

go = {0: (0,1), 1: (1,0), 2:(1,1)}
for i in range(n): # 행
    for j in range(2, n): # 열
        if graph[i][j] == 1:
            continue
        dp[i][j][0] = dp[i][j-1][0] + dp[i][j-1][2]
        dp[i][j][1] = dp[i-1][j][1] + dp[i-1][j][2]
        if graph[i-1][j] == 0 and graph[i][j-1] == 0:
            dp[i][j][2] = sum(dp[i-1][j-1])
    
print(sum(dp[n-1][n-1]))    