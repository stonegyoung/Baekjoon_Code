import sys
input = sys.stdin.readline

def preorder(now):
    if now != '.':
        print(now, end='')
    if di[now][0] != '.':
        preorder(di[now][0])
    if di[now][1] != '.':
        preorder(di[now][1])

def inorder(now):
    if di[now][0] != '.':
        inorder(di[now][0])
    if now != '.':
        print(now, end='')
    if di[now][1] != '.':
        inorder(di[now][1])

def postorder(now):
    if di[now][0] != '.':
        postorder(di[now][0])
    if di[now][1] != '.':
        postorder(di[now][1])
    if now != '.':
        print(now, end='')

n = int(input())
di = {}
for _ in range(n):
    now, l, r = input().split()
    di[now] = [l, r]
    
preorder('A')
print()
inorder('A')
print()
postorder('A')
print()

