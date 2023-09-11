def solution(n, arr1, arr2):
    answer = []
    for a, b in zip(arr1, arr2):
        temp = ''
        a_str = bin(a)[2:]
        b_str = bin(b)[2:]
        a_str = (n-len(a_str))*'0' + a_str
        b_str = (n-len(b_str))*'0' + b_str
        for i, j in zip(a_str, b_str):
            if i == '0' and j == '0':
                temp += ' '
            else:
                temp += '#'
        answer.append(temp)
    return answer