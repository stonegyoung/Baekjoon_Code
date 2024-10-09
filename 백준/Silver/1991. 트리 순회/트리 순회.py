# 8tl 55qns
import sys
from collections import deque
n = int(input())

tree = {}
root = ''
for _ in range(n):
    a,b,c = list(input().split())
    tree[a] = [b,c]
    

def pre(node):
    print(node, end='')
    
    if tree[node][0] != '.':
        pre(tree[node][0])
    if tree[node][1] != '.':
        pre(tree[node][1])
            
def post(node):
    if tree[node][0] != '.':
        post(tree[node][0])
    if tree[node][1] != '.':
        post(tree[node][1])
    print(node, end='')

def infix(node):
    if tree[node][0] != '.':
        infix(tree[node][0])
    print(node, end='')
    if tree[node][1] != '.':
        infix(tree[node][1])
    
root = 'A'
pre(root)
print()
infix(root)
print()
post(root)