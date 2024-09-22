# 11시 7분
# a-b
import sys
input = sys.stdin.readline
na, nb = map(int, input().split())

a = set(map(int, input().split()))
b = set(map(int, input().split()))

lists = list(a-b)
if len(lists) == 0:
    print(0)
else:
    print(len(lists))
    for l in sorted(lists):
        print(l,  end=' ')
