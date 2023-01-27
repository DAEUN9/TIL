import sys

sys.stdin = open("input.txt", "r")

T = int(input())
for _ in range(T):
    S = input()
    start = 0
    end = len(S)-1
    cnt = 0
    while start<=end:
        if S[start] == S[end]:
            start += 1
            end -= 1
            continue
        cnt += 1
        if (S[start] == S[end-1]) and (S[start+1] == S[end]):
            temp_start = start
            temp_end = end-1
            while temp_start <= temp_end:
                if (S[temp_start] == S[temp_end]):
                    temp_start += 1
                    temp_end -= 1
                    continue
                start += 1
                break
            else:
                end -= 1
        elif (S[start] == S[end-1]):
            end -= 1
        elif (S[start+1] == S[end]):
            start += 1
        if cnt == 2:
            break
    print(cnt, S)