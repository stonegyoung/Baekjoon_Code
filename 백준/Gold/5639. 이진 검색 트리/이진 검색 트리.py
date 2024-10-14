import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
 
# def post(node):
#     if node.left != None:
#         post(node.left)    
#     if node.right != None:
#         post(node.right)
#     print(node.node)

# class Node:
#     def __init__(self, node):
#         self.node = node
#         self.left = None
#         self.right = None
    
#     def plus(self, res):
#         if self.left == None and self.node>res.node:
#             self.left = res
#         elif self.right == None and self.node<res.node:
#             self.right = res
            
#         elif self.node > res.node:
#             self.left.plus(res)
#         else:
#             self.right.plus(res)
# i = True
# while True:
#     try:
#         if i:
#             root  = Node(int(input()))
#             i = False
#         else:
#             a = Node(int(input()))
#             root.plus(a)
#     except:
#         break
# post(root)
   
def post(lists):
    mid = lists[0]
    left = [i for i in lists if mid>i]
    right = [i for i in lists if mid<i]
    if len(left) != 0:
        post(left)
    if len(right) != 0:
        post(right)
    print(mid)
    
lists = []
while True:
    try:
        lists.append(int(input()))
    except:
        break
post(lists)
