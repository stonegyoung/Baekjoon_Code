# 재귀
import sys
input = sys.stdin.readline

N, r, c = map(int, input().split())
n = 2 ** N

cnt = 0
def z(targetr, targetc, n):
    global cnt
    if n == 2:
        if targetr == 0 and targetc == 0:
            return cnt
        elif targetr == 0 and targetc == 1:
            return cnt+1
        elif targetr == 1 and targetc == 0:
            return cnt+2
        else:
            return cnt+3
    n = n//2
    if targetr < n and targetc < n: # 왼위
        return z(targetr, targetc, n)
    elif  targetr < n and targetc >= n: # 오위
        cnt += n**2
        return z(targetr, targetc-n,n)
        
    elif targetr >= n and targetc < n: # 왼아
        cnt += 2*(n**2)
        return z(targetr-n, targetc, n)
    else: # 오아
        cnt += 3*(n**2)
        return z(targetr-n, targetc-n, n)
        
    
print(z(r,c,n))