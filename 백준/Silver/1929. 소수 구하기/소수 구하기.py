# 10시 39분~
from sys import stdin
import math

m, n = map(int, stdin.readline().split())

for mn in range(m, n+1):
    r = True
    if mn == 1:
        continue
    if mn <= 5:
        for i in range(2, mn):
            if mn%i==0:
                r = False
                break
    else:
        for i in range(2, int(math.sqrt(mn))+1):
            if mn%i==0:
                r = False
                break

    if r==True:
        print(mn)