from sys import stdin

n = int(stdin.readline())

data = []
for _ in range(n):
    x, y = map(int, stdin.readline().split())
    data.append((x,y))
    
data.sort(key=lambda x: (x[1], x[0]))
for d in data:
    print(d[0], d[1])