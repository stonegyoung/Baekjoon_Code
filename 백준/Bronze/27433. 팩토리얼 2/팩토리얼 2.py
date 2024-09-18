n = int(input())

def fib(n):
    dp = [0] * (n+1)
    dp[0] = 1
    
    if n>0:
        dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] * i
        
    print(dp[n])
    
fib(n)