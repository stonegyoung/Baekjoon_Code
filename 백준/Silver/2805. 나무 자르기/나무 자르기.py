# 4시 7분
from sys import stdin

# 나무 수, 가져갈 길이
n, m = map(int, stdin.readline().split())

trees = list(map(int, stdin.readline().split()))

# 절단기 자르기
start = 0
end = max(trees)

def bs(start, end):
    # 자를 길이
    
    while start <= end:
        mid = (start+end)//2
        total = 0
        for tree in trees:
            if tree > mid:
                total += tree - mid
        
        if total == m:
            return mid
        
        if total < m: # 절단기 아래로
            end = mid - 1
            
        else: # 절단기 더 위로
            start = mid + 1
            
    return end

print(bs(start, end))
            