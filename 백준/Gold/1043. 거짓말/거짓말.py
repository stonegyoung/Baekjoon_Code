# 12tl 52qns
# bfs
import sys
from collections import deque
input = sys.stdin.readline

def bfs(num, visited):
    idx = []
    q = deque(num)
    for n in num:
        visited[n] = 1
        idx.append(n)
    while q:
        v = q.popleft()
        for g in graph[v]:
            if visited[g] == 0:
                visited[g] = 1
                idx.append(g)
                q.append(g)
    return idx
    

n, m = map(int, input().split())
know, *num = map(int, input().split())
# print(know)
# print(num)
graph = [set() for _ in range(n+1)]
party = []
for _ in range(m):
    come, *people = map(int, input().split())
    party.append(set(people))
    for i in people:
        for p in people:
            if i != p:
                graph[i].add(p)
if know == 0:
    print(m)
else:
    # print(graph)
    visited = [0] * (n+1)
    truth = bfs(num, visited)
    # print(party)
    # print(truth)
    cnt = 0
    for par in party:
        cnt += 1
        for t in truth:
            if t in par:
                cnt -= 1
                break

    print(cnt)
