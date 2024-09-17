from sys import stdin
t = int(stdin.readline())

def dfs(now_x, now_y):
    # visit
    visited.append((now_x, now_y))
    
    # festival이랑 거리 봐 되면 happy
    x = now_x-festival_x if now_x > festival_x else festival_x-now_x
    y = now_y-festival_y if now_y > festival_y else festival_y-now_y
    if x + y <= 1000:
        return True
    # 안되면 다른 store 가
    for s_x, s_y in store:
        if (s_x, s_y) not in visited:
            # 지금 위치랑 store 위치 확인
            d_x = now_x-s_x if now_x > s_x else s_x-now_x
            d_y = now_y-s_y if now_y > s_y else s_y-now_y
        
            if d_x + d_y <= 1000:
                # 1000 되면 가
                if dfs(s_x, s_y):
                    return True
    return False
            
    
    
result = []
for _ in range(t):
    n = int(stdin.readline()) # 편의점 개수
    home_x, home_y = map(int, stdin.readline().split())
    store = []    
    for _ in range(n):
        store.append(list(map(int, stdin.readline().split())))
    
    festival_x, festival_y =map(int, stdin.readline().split())
    
    x = festival_x-home_x if festival_x > home_x else home_x-festival_x
    y = festival_y-home_y if festival_y > home_y else home_y-festival_y
        
    if x+y<=1000:
        print('happy')
    else:
        hp = 'sad'
        for store_x, store_y in store:
            x = store_x-home_x if store_x > home_x else home_x-store_x
            y = store_y-home_y if store_y > home_y else home_y-store_y
            if x+y<=1000:
                visited = []
                # 지금에서 1000 안쪽의 store 들려
                res = dfs(store_x, store_y)
                if res == 1:
                    hp = 'happy'
                    break  
        print(hp)
            