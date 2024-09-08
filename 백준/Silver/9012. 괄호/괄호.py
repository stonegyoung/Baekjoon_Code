# https://www.acmicpc.net/problem/9012
# 3시 10분
from sys import stdin

n = int(stdin.readline())
res = ['YES'] * n
for i in range(n):
    st = (stdin.readline().strip())
    
    if st.count('(') != st.count(')'):
        res[i] = 'NO'
        continue
    cnt = 0
    for s in st:
        if s=='(':
            cnt += 1
        else:
            cnt -= 1
            if cnt < 0:
                res[i] = 'NO'
                continue
            
for r in res:
    print(r)