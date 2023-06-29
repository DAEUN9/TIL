def solution(s):
    li = s.split()
    answer = []
    for l in li:
        temp = ''
        for i in range(len(l)):
            if i%2:
                temp += l[i].lower()
            else:
                temp += l[i].upper()
        answer.append(temp)
    return ' '.join(answer)