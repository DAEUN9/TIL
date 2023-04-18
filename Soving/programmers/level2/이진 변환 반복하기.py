def solution(s):
    answer = [0, 0]
    while s != "1":
        answer[1] += s.count("0")
        s = s.replace("0", "")
        s = format(len(s), 'b')
        answer[0] += 1

    return answer
inn = "110010101001"
a = solution(inn)
print(a)