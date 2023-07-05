import sys
sys.setrecursionlimit(10**6)


        
def solution(nodeinfo):
    tree = dict()
    
    def make_tree(parent, node):
        if not tree[parent][0] and parent[0] > node[0]:
            tree[parent][0] = node
        elif not tree[parent][1] and parent[0] < node[0]:
            tree[parent][1] = node
        elif tree[parent][0][0] > node[0]:
            make_tree(parent[1], node)
        else:
            make_tree(parent[0], node)
        
    for i in range(len(nodeinfo)):
        nodeinfo[i].append(i+1)
    for j in range(len(nodeinfo)):
        tree[j+1] = [None, None]
    nodeinfo.sort(key = lambda x : (-x[1], x[0]))
    parent = nodeinfo[0]
    for node in nodeinfo[1:]:
        make_tree(parent, node)
    

        
    answer = [[]]
    return answer