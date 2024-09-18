# 11시 7분
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

set_s = set()
for _ in range(n):
    set_s.add(input())
    
cnt = 0
for _ in range(m):
    data = input()
    if data in set_s:
        cnt += 1
print(cnt)