# 3시 34분
import sys
input = sys.stdin.readline

N = list(map(int, input().rstrip()))

N.sort(reverse=True)
for n in N:
    print(n, end='')