def solution(numbers):
    answer = []
    for i in numbers:
        num = i
        cnt = 0
        while i % 2 == 1:
            cnt += 1
            i //= 2
        answer.append(num + 2**(cnt - 1) if cnt != 0 else num + 1)

    return answer