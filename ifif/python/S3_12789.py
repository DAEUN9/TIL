import sys
sys.stdin = open("input.txt", "r")
N = int(input())
start = list(map(int, input().split()))
end = [0]
temp = []
while True:
    if len(start) == 0:
        if temp:
            if temp[-1] != end[-1]+1:
                break
            else:
                end.append(temp.pop())
        else:
            break
    elif start[0] != end[-1]+1:
        if temp and temp[-1] == end[-1]+1:
            end.append(temp.pop())
        else:
            temp.append(start.pop(0))
    else:
        end.append(start.pop(0))
if len(end) == N+1:
    print("Nice")
else:
    print("Sad")