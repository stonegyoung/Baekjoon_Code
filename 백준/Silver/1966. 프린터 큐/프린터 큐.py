import sys
input = sys.stdin.readline
from collections import deque

t = int(input())

def cnt_max(lists, sortlist):
    i = 0
    cnt = 0
    while True:
        if lists[i][0] == sortlist[cnt][0]:
            if lists[i][1] == m:
                return cnt+1
            else:
                cnt += 1
        else:
            lists.append((lists[i]))   
        i += 1 

for _ in range(t):
    n, m = map(int, input().split())
    imp = list(map(int, input().split()))
    
    if n == 1:
        print(1)
    else:
        lists = deque([(num, i) for i, num in enumerate(imp)])
        sortlist = sorted(lists, reverse=True)
        print(cnt_max(lists, sortlist))
        # print(sortlist)