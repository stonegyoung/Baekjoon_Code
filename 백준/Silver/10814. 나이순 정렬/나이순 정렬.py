# 3시 9분
# 나이 -> 가입
from sys import stdin
n = int(stdin.readline())

data = []
for i in range(n):
    age, name = stdin.readline().split()
    data.append((int(age), i, name))
    
data.sort(key=lambda x: (x[0],x[1]))
for age, _, name in data:
    print(age, name)