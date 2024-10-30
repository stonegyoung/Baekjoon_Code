# 10시 16분
import sys
input = sys.stdin.readline

n = int(input())

if n==1:
    print(0)
    print(1)
else:
    dp = [[0,0] for _ in range(n+1)]
    try:
        dp[2] = [1, 1] # 다음 숫자, 총 숫자
        dp[3] = [1, 1]
    except:
        pass
    for i in range(4, n+1):
        dp[i] = [i-1, dp[i-1][1]+1]
        if i%3 == 0:
            n3 = i//3
            if dp[n3][1]+1 < dp[i][1]:
                dp[i] = [n3, dp[n3][1]+1]
        if i%2 == 0:
            n2 = i//2
            if dp[n2][1]+1 < dp[i][1]:
                dp[i] = [n2, dp[n2][1]+1]
        
    
    print(dp[n][1])
    print(n, end=' ')
    i = n
    while i != 1:
        print(dp[i][0], end=' ')
        i = dp[i][0]