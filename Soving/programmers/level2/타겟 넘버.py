def solution(numbers, target):
    global answer
    answer = 0
    dfs(0, 0, numbers, target)
    return answer

def dfs(idx, curr, numbers, target):
    global answer
    if idx == len(numbers):
        if curr == target:
            answer += 1
        return
    dfs(idx+1, curr+numbers[idx], numbers, target)
    dfs(idx+1, curr-numbers[idx], numbers, target)
