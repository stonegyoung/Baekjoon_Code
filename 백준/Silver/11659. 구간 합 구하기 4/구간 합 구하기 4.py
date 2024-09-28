# 4시
# 누적합
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nlist = list(map(int, input().split()))

sumlist = [0] * n
sumlist[0] = nlist[0]
for i in range(1, n):
    sumlist[i] = sumlist[i-1] + nlist[i]

# print(sumlist)
for _ in range(m):
    start, end = map(int, input().split())
    start -= 1
    end -= 1
    if start == end: # 똑같으면
        print(nlist[start])
    elif start == 0: # 처음부터
        print(sumlist[end])
    else:
        print(sumlist[end]- sumlist[start-1])