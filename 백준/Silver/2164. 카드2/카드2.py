# https://www.acmicpc.net/problem/2164
# 3시 1분~
from collections import deque
from sys import stdin

n = int(stdin.readline())

lists = deque([i for i in range(1, n+1)])
while True:
    if len(lists) == 1:
        break
    lists.popleft()
    v = lists.popleft()
    lists.append(v)
    
print(lists[0])