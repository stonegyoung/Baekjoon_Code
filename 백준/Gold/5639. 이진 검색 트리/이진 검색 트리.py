import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def post(start, end):
    if start > end:
        return
    mid = lists[start]
    change = end+1
    for i in range(start+1, end+1):
        if mid < lists[i]:
            change = i
            break
    post(start+1, change-1)
    post(change, end)
    print(mid)
        
    
lists = []
while True:
    try:
        lists.append(int(input()))
    except:
        break
post(0, len(lists)-1)