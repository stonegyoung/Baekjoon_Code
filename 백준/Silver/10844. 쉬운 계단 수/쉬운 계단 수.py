# 10시 27분

# 앞자리수 *2 (9는 1개 -> 8, 0은 1개 -> 1)
 
n = int(input())
dp = [0] * (10)
a = [0,1,1,1,1,1,1,1,1,1]

for i in range(2, n+1):
    for j in range(0, 10):
        dp[j] = (a[j-1] if j-1 >= 0 else 0) + (a[j+1] if j+1 < 10 else 0)
    
    for i in range(0, 10):
        a[i] = dp[i]

print(sum(a) % 1000000000)