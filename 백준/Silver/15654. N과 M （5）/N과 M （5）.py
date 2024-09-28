# 12시 19분
import sys
input = sys.stdin.readline

def bt(idx, letter):
    if idx >= m:
        print(' '.join(letter))
        return
    
    for i in lists:
        if check(letter, str(i)):
            bt(idx+1, letter+[str(i)])
            
def check(letter, s):
    if len(letter) == 0:
        return True
    if s in letter:
        return False
    else:
        return True
    
n, m = map(int, input().split())

lists=list(map(int, input().split()))
lists.sort()

bt(0, [])
