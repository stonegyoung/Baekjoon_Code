n = int(input())
'''
1
2~7 6개 -> 2
8~19 12개 -> 3
20~37 18개 -> 4
38~61 24개 -> 5
'''
n -= 1
cnt = 1
i = 1
while n > 0:
    n = n - (6*i)
    cnt += 1
    i += 1
print(cnt)