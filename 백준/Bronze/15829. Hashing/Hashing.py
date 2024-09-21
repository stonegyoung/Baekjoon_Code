import sys
input = sys.stdin.readline

l = int(input())
st = input().rstrip()

res = 0
for i in range(l):
    res += (ord(st[i])-96)* (31**i) 
    
print(res % 1234567891)