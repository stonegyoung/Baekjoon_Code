# 12시 18분 이진
import sys
input = sys.stdin.readline

m, n = map(int, input().split())
snack = list(map(int, input().split()))

def bs(start, end):
    while start<=end:
        mid = (start+end)//2
        if end != 0 and mid == 0:
            mid = 1
        # 자르는 수를 mid로
        
        cnt = 0
        s = n-1
        while snack[s] >= mid and s>=0:
            cnt += snack[s]//mid
            s -= 1

        if cnt >= m: # 너무 작게 자름 -> 더 크게
            start = mid + 1
        else: # 너무 크게 자름 -> 더 작게
            end = mid -1
    return end

snack.sort()
res = bs(1, max(snack))
print(0 if res == -1 else res)