import sys
sys.stdin = open("input.txt", "r")

string = input()
def findGroup(num):
    idx = -1
    cnt = 0
    while len(string) > idx+1:
        idx += 1
        if string[idx] == num:
            cnt += 1
            while len(string) > idx+1 and string[idx+1] == num:
                    idx += 1
    return cnt

answer = min(findGroup("1"), findGroup("0"))
print(answer)