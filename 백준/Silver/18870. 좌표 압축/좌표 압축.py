# 5시 25분
from sys import stdin

n = int(stdin.readline())

data = list(map(int, stdin.readline().split()))

d = dict()
for idx, nn in enumerate(sorted(set(data))):
    d[nn] = idx # 몇 번째인지
    
# print(d)
    
for dd in data:
    # d보다 작은 데이터 수 찾기
    print(d[dd], end=' ')


