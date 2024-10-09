# 8tl 55qns
import sys
from collections import deque
n = int(input())

tree = {}
root = ''
for i in range(n):
    a,b,c = list(input().split())
    if i == 0:
        root = a
    tree[a] = [b,c]
    

def pre(node):
    if node == '.':
        return
    if node not in visited:
        print(node, end='')
        visited.add(node)
    
    pre(tree[node][0])
    pre(tree[node][1])
            
def post(node):
    if node not in visited and node != '.':
        visited.add(node)
    if tree[node][0] != '.':
        post(tree[node][0])
    if tree[node][1] != '.':
        post(tree[node][1])
    print(node, end='')

def infix(node):
    if node not in visited and node != '.':
        visited.add(node)
    if tree[node][0] != '.':
        infix(tree[node][0])
    print(node, end='')
    if tree[node][1] != '.':
        infix(tree[node][1])
    
visited = set()
pre(root)
print()
visited = set()
infix(root)
print()
visited = set()
post(root)