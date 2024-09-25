# 8시 36분
import sys
input = sys.stdin.readline

n = int(input())

# 0, 1로 끝나는 거
dp = [[0,0] for _ in range(n+1)]

# 1
dp[1] = [0, 1]

if n!= 1:
    # 10 
    dp[2] = [1, 0]

for i in range(3, n+1):
    dp[i][0] = dp[i-1][0] + dp[i-1][1]  # 0으로 끝나는 거: 0 다음에, 1 다음에
    dp[i][1] = dp[i-1][0] # 1로 끝나는거: 0 다음에

# print(dp)
print(sum(dp[n]))