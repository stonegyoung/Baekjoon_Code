# 2시 35분
from sys import stdin

n, m = map(int, stdin.readline().split())
voca = {}
voca_num = ['' for _ in range (100001)]
for i in range(1, n+1):
    data = stdin.readline().rstrip()
    voca[data] = i
    voca_num[i] = data
    
for _ in range(m):
    ques = stdin.readline().rstrip()
    if ques.isdigit():
        print(voca_num[int(ques)])
    else:
        print(voca[ques])