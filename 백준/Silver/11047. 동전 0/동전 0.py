n, k = map(int, input().split())

money = []
for _ in range(n):
    money.append(int(input()))

cnt = 0
for m in money[::-1]:
    if k//m == 0:
        continue
    else:
        cnt += k//m
        k = k % m
print(cnt)