# 10시 7분
# bt 중복체크, 오름차순
import sys
input = sys.stdin.readline

last = -1
def bt(idx, letter):
    global last
    if idx >= m:
        print(' '.join(letter))
        return
    for i in range(n):
        if nlist[i] >= last:
            if i == 0:
                last = nlist[i]
                bt(idx+1, letter + [str(nlist[i])])
            if i > 0 and nlist[i-1] != nlist[i] : # 중복 체크
                last = nlist[i]
                bt(idx+1, letter + [str(nlist[i])])
    last = -1

n, m = map(int, input().split())
nlist = list(map(int, input().split()))

nlist.sort()
visited = [False] * n
bt(0, [])