from sys import stdin

n = int(stdin.readline())
cards = list(map(int, stdin.readline().split()))

m = int(stdin.readline())
count_card = list(map(int, stdin.readline().split()))

d = dict()
for c in cards:
    d[c] = d.get(c, 0) + 1
    
for cc in count_card:
    print(d[cc] if cc in d else 0, end=' ')