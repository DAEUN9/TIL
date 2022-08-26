# 성격 유형 검사하기
# kakao

# https://school.programmers.co.kr/learn/courses/30/lessons/118666

def solution(survey, choices):
    answer = ''
    mbti = ['RT', 'CF', 'JM', 'AN']
    d = dict()
    for i in range(len(choices)):
        if choices[i]< 4:
            a = d.get(survey[i][0], 0)
            d[survey[i][0]] = a + choices[i]
        elif choices[i] > 4:
            a = d.get(survey[i][1], 0)
            d[survey[i][1]] = a + choices[i]-4
    print(d)
    for m in mbti:
        a = d.get(m[0], 0)
        b = d.get(m[1], 0)
        if a>=b:
            answer += m[0]
        else:
            answer += m[1]
    return answer


answer = solution(["TR", "RT", "TR"], [7, 1, 3])
print(answer)