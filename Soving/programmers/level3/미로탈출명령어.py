def solution(n, m, x, y, r, c, k):
    global answer
    # 시작점 x, y
    # 도착점 r, c
    answer = 'z'*k

    dfs(x-1, y-1, r-1, c-1, n, m, '', k)
    return answer

def dfs(a, b, r, c, n, m, s, k):
    global answer
    if len(s) == k:
        if a==r and b==c and answer > s:
            answer = s
        return
    if b-1 >= 0:
        dfs(a, b-1, r, c, n, m, s+'l', k)
    if b+1 < n:
        dfs(a, b+1, r, c, n, m, s+'r', k)
    if a-1 >= 0:
        dfs(a-1, b, r, c, n, m, s+'u', k)
    if a+1 < m:
        dfs(a+1, b, r, c, n, m, s+'d', k)

answer = solution(3,	4,	2,	3,	3,	1,	5)
print(answer)