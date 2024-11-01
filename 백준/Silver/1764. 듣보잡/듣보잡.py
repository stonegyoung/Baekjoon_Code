# 5시 50분
# set
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nlist = set()
for _ in range(n):
    nlist.add(input().rstrip())
    
mlist = set()
for _ in range(m):
    mlist.add(input().rstrip())

s = nlist & mlist
print(len(s))
print('\n'.join(sorted(list(s))))