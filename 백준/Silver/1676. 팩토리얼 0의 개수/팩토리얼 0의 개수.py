# 8시 46분

import sys

input = sys.stdin.readline

n = int(input())

res = 1
for i in range(1, n+1):
    res *= i
    
res = str(res)
cnt = 0
for i in range(len(res)-1, -1, -1):
    if res[i] == '0':
        cnt += 1
    else:
        break
    
print(cnt)