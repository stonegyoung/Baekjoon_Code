# 12tl 35qns
# 두 사람이 친구 or 겹지인까지 ㅇㅋ
import sys
input = sys.stdin.readline

n = int(input())
# 친구를 리스트에
graph = [[] for _ in range(n)]
for i in range(n):
    lists = list(input().rstrip())
    for j in range(n):
        if lists[j] == 'Y':
            graph[j].append(i)
# print(graph)

def friend(idx, g):
    fr = set(g)
    for i in g:
        for j in graph[i]:
            if j not in fr and j != idx:
                fr.add(j)
    # print(fr)
    return len(fr)

maxi = 0
for i in range(n):
    a = friend(i, graph[i])
    maxi = max(a, maxi)
    
print(maxi)