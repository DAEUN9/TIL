from collections import deque




def solution(queue1, queue2):
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    answer = 0
    A, B = sum(queue1), sum(queue2)
    max_num = len(queue1) + len(queue2)
    if (A+B)%2:
        return -1
    while sum(queue1) != sum(queue2):
        if answer >= max_num:
            return -1
        while queue1 and A > B:
            temp = queue1.popleft()
            queue2.append(temp)
            answer += 1
            A -= temp
            B += temp
            
        while queue2 and A < B:
            temp = queue2.popleft()
            queue1.append(temp)
            answer += 1
            A += temp
            B -= temp
    return answer