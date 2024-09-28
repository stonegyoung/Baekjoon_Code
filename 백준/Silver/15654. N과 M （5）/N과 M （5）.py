# 12시 19분~51분
import sys
input = sys.stdin.readline

# def bt(idx, letter):
#     if idx >= m:
#         print(' '.join(letter))
#         return
    
#     for i in lists:
#         if check(letter, str(i)):
#             bt(idx+1, letter+[str(i)])
            
# def check(letter, s):
#     if len(letter) == 0:
#         return True
#     if s in letter:
#         return False
#     else:
#         return True
    
def dfs(idx, letter):
    if idx >= m:
        print(' '.join(letter))
        return
    
    for i in range(len(lists)):
        if visited[i]:
            continue
        visited[i] = True
        dfs(idx+1, letter+[str(lists[i])])
        visited[i] = False
        
n, m = map(int, input().split())

lists=list(map(int, input().split()))
lists.sort()
visited = [False] * n
dfs(0, [])
# bt(0, [])
