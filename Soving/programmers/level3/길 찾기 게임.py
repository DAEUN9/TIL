import sys

sys.setrecursionlimit(10 ** 6)


def solution(nodeinfo):
    tree = dict()
    answer = [[], []]

    def preorder(root):
        if root:
            answer[0].append(root[2])
            preorder(tree[root][0])
            preorder(tree[root][1])

    def postorder(root):
        if root:
            postorder(tree[root][0])
            postorder(tree[root][1])
            answer[1].append(root[2])

    def make_tree(parent, node):
        if parent[0] > node[0]:
            if not tree[parent][0]:
                tree[parent][0] = node
            else:
                make_tree(tree[parent][0], node)
        elif parent[0] < node[0]:
            if not tree[parent][1]:
                tree[parent][1] = node
            else:
                make_tree(tree[parent][1], node)

    for i in range(len(nodeinfo)):
        nodeinfo[i].append(i + 1)
    nodeinfo = list(map(tuple, nodeinfo))

    for node in nodeinfo:
        tree[node] = [None, None]
    nodeinfo.sort(key=lambda x: (-x[1], x[0]))
    parent = nodeinfo[0]
    for node in nodeinfo[1:]:
        make_tree(parent, node)
    preorder(nodeinfo[0])
    postorder(nodeinfo[0])
    return answer

nodeinfo = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]
result = [[7,4,6,9,1,8,5,2,3],[9,6,5,8,1,4,3,2,7]]

print(solution(nodeinfo))