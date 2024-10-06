# 4시 18분
import sys
input = sys.stdin.readline

def bt(idx, letter):
    if idx >= m:
        print(' '.join(letter))
        return
    ascending = -1 if len(letter) == 0 else int(letter[-1])
    for i in range(n):
        if ascending <= nlist[i] and visited[i]==False: # 같은 레벨에서 비내림차순 확인
            if i > 0 and nlist[i] == nlist[i - 1] and not visited[i - 1]: # 같은 레벨에서 중복 방지
                continue
            visited[i] = True
            bt(idx+1, letter+[str(nlist[i])])
            visited[i] = False
            
            
n, m = map(int, input().split())
nlist = list(map(int, input().split()))
nlist.sort()
visited = [False] * n
bt(0, [])