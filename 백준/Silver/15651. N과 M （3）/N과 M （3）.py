# 11tl 59분
import sys
input = sys.stdin.readline

def bt(idx, letter):
    if idx >= m:
        print(' '.join(letter))
        return
    for i in lists:
        bt(idx+1, letter+str(i))
n, m = map(int, input().split())
lists = [i for i in range(1, n+1)]

bt(0, '')