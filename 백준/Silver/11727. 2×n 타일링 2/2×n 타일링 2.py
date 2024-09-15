from sys import stdin

n = int(stdin.readline())

dp = [0] * (n+1)

try:
    dp[1] = 1 # 1X2
    dp[2] = 3 # 1X2 두 개, 2X1 두 개, 2X2
except:
    pass

# i-2는 두 개(1X2 두 개는 중복됨) i-1은 1개
for i in range(3, n+1):
    dp[i] = ((dp[i-2])*2 + dp[i-1]) %  10007
    
print(dp[n])