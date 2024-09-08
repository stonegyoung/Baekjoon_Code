# https://www.acmicpc.net/problem/9012
# 3시 10분~3시 21분
from sys import stdin

n = int(stdin.readline())
for i in range(n):
    st = (stdin.readline().strip())
    res = 'YES'
    if st.count('(') != st.count(')'):
        res ='NO'
        print(res)
        continue
    cnt = 0
    for s in st:
        if s=='(':
            cnt += 1
        else:
            cnt -= 1
            if cnt < 0:
                res = 'NO'
                continue
    print(res)