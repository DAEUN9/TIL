def solution(n, build_frame):
    answer = []
    for x, y, a, b in build_frame:
        if b == 1:
            if check(answer, x, y, a):
                answer.append([x, y, a])
        else:
            answer.remove([x, y, a])
            for q, w, e in answer:
                if check(answer, q, w, e):
                    continue
                answer.append([x, y, a])
                break
    answer.sort()
    return answer


def check(answer, x, y, structure):
    if structure == 0:  # 기둥
        if [x, y - 1, 0] in answer:
            return True
        if y == 0:
            return True
        if [x, y, 1] in answer:
            return True
        if [x - 1, y, 1] in answer:
            return True
        return False
    if structure == 1:  # 보
        if [x - 1, y, 1] in answer and [x + 1, y, 1] in answer:
            return True
        if [x, y - 1, 0] in answer:
            return True
        if [x + 1, y - 1, 0] in answer:
            return True
        return False
