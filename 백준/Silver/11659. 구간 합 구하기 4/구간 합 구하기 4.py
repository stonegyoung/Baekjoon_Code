# 4시
# 누적합
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nlist = list(map(int, input().split()))

sumlist = [0] * (n+1)

for i in range(1, n+1):
    sumlist[i] = sumlist[i-1] + nlist[i-1]
#print(sumlist)
for _ in range(m):
    start, end = map(int, input().split())
    
    print(sumlist[end]- sumlist[start-1])