# https://programmers.co.kr/learn/courses/30/lessons/42860?language=python3

def solution(name):
    answer = 0
    length = len(name)
    min_move = length - 1
    for i in range(length):
        answer += min(ord(name[i]) - ord("A"), ord("Z") + 1 - ord(name[i]))

        next = i + 1
        while next < length and name[next] == 'A':
            next += 1

        min_move = min(min_move, 2 * i + length - next, i + 2 * (length - next))
    answer += min_move

    return answer