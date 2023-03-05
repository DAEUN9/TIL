import sys
sys.stdin = open("input.txt", "r")
A = list(map(int, list(input())))
B = list(map(int, list(input())))
temp = []
for a, b in zip(A, B):
    temp.append(a)
    temp.append(b)
while len(temp)>2:
    temp2 = []
    for i in range(1, len(temp)):
        temp2.append(int(str(temp[i-1]+temp[i])[-1]))
    temp = temp2
for t in temp:
    print(t, end="")