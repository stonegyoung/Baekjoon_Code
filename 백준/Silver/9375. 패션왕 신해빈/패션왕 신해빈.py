# 11시 14분
# 입거나 안 입거나 - 다 안 입는 경우(1)
import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    dic = dict()
    for _ in range(n):
        wear, what = input().split()
        dic[what] = dic.get(what, 0) + 1
    
    res = 1
    for i in dic.values():
        res *= (i+1)
    print(res-1)