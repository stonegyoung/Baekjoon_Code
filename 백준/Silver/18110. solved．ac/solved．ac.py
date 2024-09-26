# 4시 1분

import sys
input = sys.stdin.readline

# 반올림 함수
def round(n):
    if n -int(n) >= 0.5:
        return int(n)+1
    else:
        return int(n)

n = int(input())
if n == 0:
    print(0)
else:
    solved = [int(input()) for _ in range(n)]

    # 정렬
    solved.sort()

    # 절사평균
    m = round(n * 0.15)
    print(round(sum(solved[m:n-m]) / (n-(2*m))))