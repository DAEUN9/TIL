# 팩토리얼 0의 개수
# https://www.acmicpc.net/problem/1676

N = int(input())
fn = 1
for i in range(N+1):
    if i == 0:
        fn *= 1
    else:
        fn *= i
answer = 0
for w in str(fn)[::-1]:
    if w == '0':
        answer += 1
    else:
        break
print(answer)
