def rev():
    A, B, C = map(int, input().split())
    if B >= C:
        return -1
    return A//(C-B)+1
print(rev())