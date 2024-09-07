from sys import stdin

n = int(stdin.readline())

data = []
for _ in range(n):
    x, y = map(int, stdin.readline().split())
    data.append((x,y))
    
data.sort(key=lambda x: (x[0], x[1]))
for d in data:
    print(d[0], d[1])