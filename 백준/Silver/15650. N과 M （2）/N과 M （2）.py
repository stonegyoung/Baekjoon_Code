# 11시 50분
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

def bt(idx, letter):
    if idx >= m:
        result.append(' '.join(letter))
        return
    for i in lists:
        if check(int(letter[-1]), i):
            bt(idx+1, letter+str(i))

# 오름차순
def check(last, now):
    if last < now:
        return True
    else:
        return False
    
result = []
lists = [i for i in range(1, n+1)]
for i in lists:
    bt(1, str(i))
    
    
for res in result:
    print(res)