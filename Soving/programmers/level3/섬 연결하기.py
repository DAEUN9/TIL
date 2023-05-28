def solution(n, costs):
    answer = 0
    parent = [i for i in range(n + 1)]
    costs.sort(key=lambda x: x[2])

    #     def same_parent(a, b, parent):
    #         if get_parent(a, parent) == get_parent(b, parent):
    #             return True
    #         return False

    def get_parent(c, parent):
        if parent[c] != c:
            parent[c] = get_parent(parent[c], parent)
        return parent[c]

    def union_parent(a, b):
        pa = get_parent(a, parent)
        pb = get_parent(b, parent)
        if pa < pb:
            parent[pb] = pa
        else:
            parent[pa] = pb

    for a, b, cost in costs:
        if get_parent(a, parent) != get_parent(b, parent):
            union_parent(a, b)
            answer += cost

    return answer
