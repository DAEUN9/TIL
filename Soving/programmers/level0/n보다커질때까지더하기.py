def solution(numbers, n):
    answer = 0
    for number in numbers:
        answer += number
        if answer > n:
            return answer
    return answer