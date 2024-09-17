from sys import stdin

n, p, q = map(int, stdin.readline().split())

arr = {0:1}
def dp(n, p, q):
    if n in arr:
        return arr[n]
    
    arr[n] = dp(n//p, p, q) + dp(n//q, p, q)
    return arr[n]
    
print(dp(n,p,q))