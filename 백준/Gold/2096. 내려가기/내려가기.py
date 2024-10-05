# 3시 40분
# dp
import sys
input = sys.stdin.readline

n = int(input())

small = [0] * 3
big = [0] * 3
for _ in range(n):
    dp = list(map(int, input().split()))
    
    small = [min(small[0] + dp[0], small[1] + dp[0]), min(small[0] + dp[1], small[1] + dp[1], small[2] + dp[1]), min(small[1] + dp[2], small[2] + dp[2])]
    
    big = [max(big[0] + dp[0], big[1] + dp[0]), max(big[0] + dp[1], big[1] + dp[1], big[2] + dp[1]), max(big[1] + dp[2], big[2] + dp[2])]
print(max(big), min(small))