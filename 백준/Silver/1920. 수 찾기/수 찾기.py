# https://www.acmicpc.net/problem/1920
# 2시 55분

from sys import stdin

n = int(stdin.readline())
n_data = set(map(int, stdin.readline().split()))
m = int(stdin.readline())
m_data = list(map(int, stdin.readline().split()))

for m_d in m_data:
    if m_d in n_data:
        print(1)
    else:
        print(0)