# 11시 49분
import sys
input = sys.stdin.readline

def bt(idx, letter):
    if idx >= m:
        print(' '.join(letter))
        return
    
    for i in nlist:
        if len(letter) == 0:
            bt(idx+1, letter + [str(i)])
        else:
            if check(int(letter[-1]), i):
                bt(idx+1, letter+[str(i)])
        
        
def check(last, now):
    if last < now:
        return True
    else:
        return False

n, m = map(int, input().split())

nlist = list(map(int, input().split()))
nlist.sort()

bt(0, [])