from sys import stdin

an, bn = map(int, stdin.readline().split())

a = list(map(int, stdin.readline().split()))
b = list(map(int, stdin.readline().split()))
print(len(set(a)-set(b)) + len(set(b)-set(a)))