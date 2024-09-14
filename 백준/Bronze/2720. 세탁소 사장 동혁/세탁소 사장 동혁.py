# 12시 5분
from sys import stdin

t = int(stdin.readline())

money = [25, 10, 5, 1]
for _ in range(t):
    d = int(stdin.readline())
    
    for m in money:
        print(d // m, end=' ')
        d = d % m