import sys
input = sys.stdin.readline

def bs(buget, start, end):
    if start > end:
        return end
    mid = (start+end)//2
    total = 0
    for b in nlist:
        if b<=mid:
            total+=b
        else:
            total+=mid
    if total == buget:
        return mid
    if total < buget:
        return bs(buget, mid+1, end)
    else:
        return bs(buget, start, mid-1)

n = int(input())
nlist = list(map(int, input().split()))
buget = int(input())
if sum(nlist) <= buget:
    print(max(nlist))
else:
    print(bs(buget, 0, buget))