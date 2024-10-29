import sys
input = sys.stdin.readline

n = int(input())
dp = [1, 1, 1] # 공백, 좌, 우
for _ in range(2, n+1):
    dp = [
        dp[0] + dp[1] + dp[2], 
        dp[0] + dp[2],
        dp[0] + dp[1]
    ]
# print(dp)
print(sum(dp)%9901)