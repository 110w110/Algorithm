import sys

N = int(sys.stdin.readline())
I = [tuple(sys.stdin.readline().split()) for _ in range(N)]
T = {}

for p,l,r in I:
    T[p] = l,r

#preorder
def preorder(v):
    if v=='.':
        return
    print(v,end='')
    preorder(T[v][0])
    preorder(T[v][1])
preorder('A')
print("")

#inorder
def inorder(v):
    if v=='.':
        return
    inorder(T[v][0])
    print(v,end='')
    inorder(T[v][1])
inorder('A')
print("")

#postorder
def postorder(v):
    if v=='.':
        return
    postorder(T[v][0])
    postorder(T[v][1])
    print(v,end='')
postorder('A')
print("")
