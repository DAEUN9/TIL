from collections import deque

def solution(people, limit):
    answer = 0
    people.sort()
    people = deque(people)
    while people:
        answer += 1
        p = people.pop()
        if people and people[0] + p <= limit:
            p += people[0]
            people.popleft()
    return answer