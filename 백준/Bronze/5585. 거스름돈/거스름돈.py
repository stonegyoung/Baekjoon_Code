n = int(input())

money = [500, 100, 50, 10, 5, 1]
k = 1000 - n
cnt = 0
for m in money:
    if k//m == 0:
        continue
    else:
        cnt += k//m
        k = k % m
print(cnt)