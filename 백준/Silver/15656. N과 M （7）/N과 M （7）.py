# 11시 57분
import sys
input = sys.stdin.readline

def bt(idx, letter):
    if idx >= m:
        print(' '.join(letter))
        return
    for i in nlist:
        bt(idx+1, letter+[str(i)])

n, m = map(int, input().split())
nlist = list(map(int, input().split()))
nlist.sort()
bt(0, [])