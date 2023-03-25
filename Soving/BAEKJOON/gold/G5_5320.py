import sys
sys.stdin = open("input.txt", "r")
T = int(input())
for _ in range(T):
    P = input()
    n = int(input())
    string = input()[1:-1]
    l = list(string.split(","))
    start = 0
    end = n
    flag = 1
    for p in P:
        if p=="R":
            flag = (flag+1)%2
        elif flag:
            start += 1
        else:
            end -= 1
    if start<=end:
        if flag:
            print("["+",".join(l[start:end])+"]")
        else:
            print("[" + ",".join(l[start:end][::-1]) + "]")
    else:
        print("error")