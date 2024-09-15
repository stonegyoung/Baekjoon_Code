n = int(input())

mini = 0
if n > 54:
    for i in range(n-54, n):
        res = i + sum([int(s) for s in str(i)])
        if res == n:
            mini = i
            break
else:
    for i in range(1, n):
        res = i + sum([int(s) for s in str(i)])
        if res == n:
            mini = i
            break
print(mini)