# 9:16
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
dp = [0] * (n+1)
vips = []
for _ in range(m):
    vip = int(input())
    vips.append(vip)

# 점화식: dp[n-2] + dp[n-1]  
# 1,2,3,4,5 까지 있다고 할 때
# dp[5] = 1,2,3을 바꾼거 5,4 + 1,2,3,4를 바꾼거 5   
if n == 1:
    print(1)
elif n==2:
    print(2)
else:
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n+1):
        dp[i] = dp[i-1]+dp[i-2]

    total = 1
    left = 1
    for v in vips:
        total *= dp[v-left]
        left = v+1
    total *= dp[n+1-left]
    print(total)