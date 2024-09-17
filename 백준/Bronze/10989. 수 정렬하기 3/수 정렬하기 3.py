from sys import stdin

n = int(stdin.readline())

# 계수 정렬
data = [0] * 10001

for _ in range(n):
    data[int(stdin.readline())] += 1
    
for i in range(len(data)):
    if data[i] != 0:
        for _ in range(data[i]):
            print(i)