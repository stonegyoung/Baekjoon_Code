from sys import stdin

m, n = map(int, stdin.readline().split())

arr = [True] * (n + 1)
arr[0] = False
arr[1] = False

for i in range(2,n+1):
    if arr[i] == True:
        j = 2
        while i*j <= n:
            arr[i*j] = False
            j+=1


for i in range(m, n+1):
    if arr[i] == True:
        print(i)