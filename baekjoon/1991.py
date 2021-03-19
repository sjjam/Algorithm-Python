# 트리 순회
# https://www.acmicpc.net/problem/1991

n = int(input())
tree = {}

for n in range(n):
    root, left, right = input().split()
    tree[root] = [left, right]

def preorder(root):
    if root != '.':
        print(root, end='')
        preorder(tree[root][0])
        preorder(tree[root][1])

def inorder(root):
    if root != '.':
        inorder(tree[root][0])
        print(root, end='')
        inorder(tree[root][1])

def postorder(root):
    if root != '.':
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')



class Node:
    def __init__(self, item, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right

n = int(input())
tree = {}

for i in range(n):
    a, b, c = input().split()
    if b == '.':
        b = None
    if c == '.':
        c = None
    tree[a] = Node(a, b, c)