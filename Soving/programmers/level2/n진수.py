# n진수
# https://programmers.co.kr/learn/courses/30/lessons/17687

def solution(n, t, m, p):
    answer = ''
    i = -1
    cnt = 0
    idx = -1
    flag = True
    while flag:
        i += 1
        curr = _10toN(i, n)
        for c in curr:
            idx += 1
            if idx%m == p-1:
                cnt += 1
                answer += c
            if cnt >= t:
                flag =False
                break
    return answer

n_dic = {
    0: '0', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9', 10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'
}

def _10toN(num, n):
    result = ''
    #(a//b, a%b)
    q, r = divmod(num, n)

    while q > 0:
        result = n_dic[r] + result
        q, r = divmod(q,n)

    result = n_dic[r] + result
    return result