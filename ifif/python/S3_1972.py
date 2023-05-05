import sys
sys.stdin = open("input.txt", "r")

def solution(string):
    N = len(string)
    for i in range(N-2):
        d = dict()
        for j in range(0, N-i-1):
            temp = string[j] + string[j+i+1]
            cnt = d.get(temp, 0)
            if cnt:
                return False
            d[temp] = 1
    return True
while True:
    string = input()
    if string == "*":
        break
    if solution(string):
        print(string, "is surprising.")
    else:
        print(string, "is NOT surprising.")
