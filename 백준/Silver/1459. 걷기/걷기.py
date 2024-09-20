# 4시 56분
import sys

input = sys.stdin.readline

# 집 위치, 한 블록 시간, 대각선 시간
x,y,w,s=map(int, input().split())

mini = min(x, y)
if 2*w <= s: # 한 블록 가는 시간이 더 빠를 때
    print(mini * 2* w + (x-mini) * w + (y-mini) * w )
else: # 대각선이 더 빠를 때
    if w>s: # 홀수번
        m = y-x if y>=x else x-y
        print((mini+m)*s if m%2==0 else mini * s + (m-1)*s + w)
    else:
        print(mini * s + (x-mini) * w + (y-mini) * w )