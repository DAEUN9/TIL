import sys
sys.stdin = open("input.txt", "r")
sys.setrecursionlimit(50000)
K = int(input())
route = list(map(int, input().split()))
tree = [[] for _ in range(K)]

def inorder(s, e, floor):
    m = (s + e) // 2
    tree[floor].append(route[m])
    if s==e:
        return
    inorder(s, m-1, floor+1)
    inorder(m+1, e, floor+1)
inorder(0, len(route)-1, 0)
for t in tree:
    print(*t)
