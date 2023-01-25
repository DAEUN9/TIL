# 문자열
# 싸이버개강총회

import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
S, E, Q = input().split()
S = list(map(int, S.split(":")))
E = list(map(int, E.split(":")))
Q = list(map(int, Q.split(":")))

name_dict = dict()
cnt = 0
def checkStart(time):
    if S[0]> time[0]:
        return True
    if S[0] == time[0] and S[1] >= time[1]:
        return True
    return False

def checkEnd(time):
    if E[0] < time[0]:
        return True
    if E[0] == time[0] and E[1] <= time[1]:
        return True
    return False

def checkQuit(time):
    if Q[0] > time[0]:
        return True
    if Q[0] == time[0] and Q[1] >= time[1]:
        return True
    return False

while True:
    chat = input().split()
    try:
        time = list(map(int, chat[0].split(":")))
    except:
        break
    person = chat[1]
    if checkStart(time):
        name_dict[person] = 0
    elif checkEnd(time) and checkQuit(time):
        num = name_dict.get(person)
        if num==0:
            name_dict[person] = 1
for v in name_dict.values():
    if v:
        cnt += 1
print(cnt)
