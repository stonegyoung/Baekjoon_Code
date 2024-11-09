import sys
input = sys.stdin.readline
T = int(input())
dp = [[0] * 31 for _ in range(31)]
for i in range(31):
    dp[i][i] = 1  # n == r일 때 (자기 자신을 선택하는 경우는 1)
    dp[i][0] = 1  # r == 0일 때 (nC0 = 1)

# DP 점화식 채우기
for i in range(1, 31):
    for j in range(1, i + 1):  # j는 i 이하로 설정
        dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
        
for _ in range(T):
    cnt = 0
    n, m = map(int, input().split())
    if n == m:
        print(1)
    else:        
        print(dp[m][n])
        
