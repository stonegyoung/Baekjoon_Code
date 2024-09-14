from sys import stdin
from collections import deque
def dp(n):
    f = [0] * (n+1)
    f[3] = 1
    f[4] = 2
    for i in range(5, n+1):
        f[i] = f[i-1] + f[i-2] + 1
    return f[n]+1

n = int(stdin.readline())
print(dp(n), n-2)