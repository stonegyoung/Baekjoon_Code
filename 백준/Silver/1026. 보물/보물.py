# https://www.acmicpc.net/problem/1026
# 9시 26분
from sys import stdin

# b가 크면 작은 거 곱한다
n = int(stdin.readline().rstrip())
A = list(map(int, stdin.readline().rstrip().split()))
B = list(map(int, stdin.readline().rstrip().split()))

total = 0
A.sort()
for i, b in enumerate(sorted(B, reverse=True)):
    total += b * A[i]
    
print(total)