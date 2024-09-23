# 2시 50분
import sys

input = sys.stdin.readline
q = []

k = int(input())

for _ in range(k):
    a = int(input())
    if a == 0:
        q.pop()
        
    else:
        q.append(a)
        
print(sum(q))