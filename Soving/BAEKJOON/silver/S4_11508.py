import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
N = int(input())
milk_list = list(int(input()) for _ in range(N))
milk_list.sort(reverse=True)
answer = 0
for i in range(0, N, 3):
    if i+1 < N:
        answer += milk_list[i + 1] + milk_list[i]
    else:
        answer += milk_list[i]
print(answer)