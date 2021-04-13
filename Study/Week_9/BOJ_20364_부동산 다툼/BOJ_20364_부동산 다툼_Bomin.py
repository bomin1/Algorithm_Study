import sys
sys.stdin = open("input.txt")

n,q = list(map(int, input().split()))
tree =[0]*(n+1)

def order(node):
    if node == 1:
        return
    if tree[node // 2] != 0:
        node = node//2
        order(node)
        return node
    return 0

for i in range(q):
    node = int(input())
    tree[node] = 1
    print(order(node))

