import sys
sys.stdin = open("input.txt", "r")

N, F = map(int, input().split()) # 맨 윗줄 숫자 개수, F는 가장 밑에있는 수
result = ""
def pascal(arr, lev):
    global N, F, result
    if result:
        return
    if N > len(arr):
        for i in range(1, F+1):
            pascal(arr+[i], lev)
    else:
        answer = [arr]
        while len(answer[-1]) > 1:
            temp = []
            for k in range(len(answer[-1])-1):
                temp.append(answer[-1][k] + answer[-1][k+1])
            answer.append(temp)
        if len(answer[-1])==1 and answer[-1][-1] == F:
            result = answer[0]
        return
pascal([], 1)
print(*result)