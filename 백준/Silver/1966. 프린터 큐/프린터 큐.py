import sys
input = sys.stdin.readline
from collections import deque

t = int(input())

def cnt_max(q, imp):
    cnt = 0
    maxi = max(q)
    while q:
        v = q.popleft()
        if v[0] == maxi[0]:
            if v[1] == m:
                return cnt+1
            else:
                cnt += 1
                maxi = max(q)
        else:
            q.append(v)    

for _ in range(t):
    n, m = map(int, input().split())
    imp = list(map(int, input().split()))
    
    if n == 1:
        print(1)
    else:
        lists = deque([(num, i) for i, num in enumerate(imp)])
        q = deque(lists)
        print(cnt_max(q, imp))
    