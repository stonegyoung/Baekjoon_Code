# 12시 8분
import sys
input = sys.stdin.readline

def bt(idx, letter, cnt):
    if idx >= m:
        result.add(letter)
        return
    
    for i in nlist:
        if check(cnt, i):
            cnt[i] -= 1
            bt(idx+1, letter+ f'{i} ', cnt)
            cnt[i] += 1
            
            
def check(cnt, i):
    if cnt[i] -1 >= 0:
        return True
    else:
        return False

n, m = map(int, input().split())
nlist = list(map(int, input().split()))
nlist.sort()

cnt = {}
for i in nlist:
    cnt[i] = cnt.get(i, 0) + 1

    
result = set()
bt(0, '', cnt)

a = []
for res in result:
    a.append(list(map(int, res.split())))
    
for i in sorted(a):
    for j in i:
        print(j, end= ' ')
    print()
