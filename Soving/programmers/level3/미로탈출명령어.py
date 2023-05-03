import sys

sys.setrecursionlimit(5000)


def solution(n, m, x, y, r, c, k):
    global answer
    # 시작점 x, y
    # 도착점 r, c
    answer = 'impossible'

    dfs(x - 1, y - 1, r - 1, c - 1, n, m, '', 0, k)
    return answer


def dfs(a, b, r, c, n, m, s, cnt, k):
    global answer
    if answer != 'impossible':
        return
    if cnt == k:
        if a == r and b == c:
            answer = s
        return
    distance = abs(a - r) + abs(b - c)
    if distance > k - cnt:
        return
    if abs(distance - (k - cnt)) % 2:
        return

    if a + 1 < n:
        dfs(a + 1, b, r, c, n, m, s + 'd', cnt + 1, k)
    if b - 1 >= 0:
        dfs(a, b - 1, r, c, n, m, s + 'l', cnt + 1, k)
    if b + 1 < m:
        dfs(a, b + 1, r, c, n, m, s + 'r', cnt + 1, k)
    if a - 1 >= 0:
        dfs(a - 1, b, r, c, n, m, s + 'u', cnt + 1, k)
