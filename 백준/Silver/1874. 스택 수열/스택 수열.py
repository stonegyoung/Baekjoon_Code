# 9시 45분~48분
# 11시 50분

import sys
input = sys.stdin.readline

n = int(input())
want = []
for _ in range(n):
    want.append(int(input()))
    
idx = 0
i = 1
# print(want)
s = ''
stack = []
while i <= n:
    stack.append(i)
    i += 1
    s += '+'
    
    while stack:
        if stack[-1] == want[idx]:
            stack.pop()
            s += '-'
            idx += 1
        else:
            break    
        

if len(stack) == 0:
    for c in s:
        print(c)
else:
    print('NO')