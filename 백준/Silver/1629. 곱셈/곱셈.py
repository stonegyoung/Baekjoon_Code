import sys
input = sys.stdin.readline

def dac(A, B, C):
    if B == 1:
        return A%C
    
    tmp = dac(A, B//2, C)
    if B%2 == 0:
        return (tmp * tmp)%C
    else:
        return (tmp * tmp * A)%C

A, B, C = map(int, input().split())
print(dac(A,B,C))
