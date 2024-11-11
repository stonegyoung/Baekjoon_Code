# 그리디
# 11시 38
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    nlist = list(map(int, input().split()))
    
    total = 0
    maxi = nlist[-1]
    for i in range(n-1, -1, -1):
        if maxi > nlist[i]:
            total += (maxi - nlist[i])
        elif maxi < nlist[i]:
            maxi = nlist[i]
    print(total)