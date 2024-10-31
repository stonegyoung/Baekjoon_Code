# 1시 48분
# 냅색
import sys
input = sys.stdin.readline

n = int(input())
hp = list(map(int, input().split()))
happy = list(map(int, input().split()))

nh = []
for tup in zip(hp, happy):
    if tup[0] < 100:
        nh.append(tup)
        
dp = [[0]* 100 for _ in range(len(nh)+1)]

for i in range(1, len(nh)+1):
    last = dp[i-1]
    now = dp[i]
    now_hp, now_happy = nh[i-1]
    
    for j in range(1, 100):
        if now_hp > j:
            now[j] = last[j] 
        else:
            now[j] = max(last[j], last[j-now_hp] + now_happy) # 안넣, 넣
            
print(dp[-1][99])