from sys import stdin

n, p, q = map(int, stdin.readline().split())

arr = {0:1}
def dp(n, p, q):
    if n in arr:
        return arr[n]
    
    if n//p in arr and n//q in arr:
        arr[n] = arr[n//p] + arr[n//q]
        return arr[n]
    elif n//q in arr:
        return arr[n//q] + dp(n//p, p, q)
    elif n//p in arr:
        return arr[n//p] + dp(n//q, p, q)
    else:
        return dp(n//p, p, q) + dp(n//q, p, q)
    
print(dp(n,p,q))