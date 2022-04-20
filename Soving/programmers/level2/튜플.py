# https://programmers.co.kr/learn/courses/30/lessons/64065

def solution(s):
    tu =[]
    answer = []
    ttmp = ''
    flag=False
    for i in s[1:]:
        if i=='{':
            tmp = []
            flag=True
        elif i.isdigit():
            ttmp += i
        elif i=='}':
            if flag:
                tmp.append(int(ttmp))
                tu.append(tmp)
                flag=False
            ttmp =''
        elif i==',':
            if flag:
                tmp.append(int(ttmp))
                ttmp = ''


    tu.sort(key=len)
    for i in range(len(tu)):
        for j in tu[i]:
            if j not in answer:
                answer.append(j)
    return answer