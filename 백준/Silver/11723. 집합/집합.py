# 9시 48분
# https://wikidocs.net/1015
# 순서가 없어서 인덱싱 기능을 이용하려면 리스트나 튜플로 변환해야 함
# 문자열도 가능
# 교집합 & 합집합 | 차집합 -
# 원소 하나 추가 add
# 여러 원소 추가 update
# 특정값 제거 remove

import sys
input = sys.stdin.readline

S = set()

m = int(input())
for _ in range(m):
    lists = input().split()
    
    if len(lists) == 1:
        if lists[0] == 'all':
            S = set([i for i in range(1, 21)])
        elif lists[0] == 'empty':
            S = set()
    else:
        x = int(lists[1])
        if lists[0] == 'add':
            S.add(x)
        elif lists[0] == 'remove':
            if x in S:
                S.remove(x)
        elif lists[0] == 'check':
            if x in S:
                print(1)
            else:
                print(0)
        elif lists[0] == 'toggle':
            if x in S:
                S.remove(x)
            else:
                S.add(x)