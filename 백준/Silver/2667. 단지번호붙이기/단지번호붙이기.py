# https://www.acmicpc.net/problem/2667
# 11시 42분
# dfs

n = int(input())

def dfs(now_x, now_y):
    global cnt
    if now_x < 0 or now_y<0 or now_x>=n or now_y>=n:
        return False
    
    if graph[now_x][now_y] == 1:
        # visit
        graph[now_x][now_y] = 0
        cnt += 1
        
        # 위 아래 간다
        dfs(now_x+1, now_y)
        dfs(now_x-1, now_y)
        dfs(now_x, now_y+1)
        dfs(now_x, now_y-1)
        return True
    else:
        return False
    
    

graph = []
total = 0
house = []
for _ in range(n):
    graph.append(list(map(int, input())))

for i in range(n):
    for j in range(n):
        cnt=0
        res = dfs(i, j)
        if res == True:
            total += 1
            house.append(cnt)
print(total)
for h in sorted(house):
    print(h)
