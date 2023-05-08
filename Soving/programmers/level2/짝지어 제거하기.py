def solution(s):
    stack = []
    for i in range(len(s)):
        if stack:
            if stack[-1] == s[i]:
                stack.pop()
            else:
                stack.append(s[i])
        else:
            stack.append(s[i])
    if stack:
        return 0
    else:
        return 1