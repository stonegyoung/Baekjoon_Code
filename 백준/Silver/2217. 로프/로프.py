import sys
input = sys.stdin.readline

n = int(input())

rope = []
for _ in range(n):
    rope.append(int(input()))
    
rope.sort()

# 얘를 넣을 때 * len()
maxi = 0
for i in range(n):
    maxi = max(maxi, rope[i] * (n-i))
    
print(maxi)