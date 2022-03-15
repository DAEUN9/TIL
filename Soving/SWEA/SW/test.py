import sys

sys.stdin = open('sample_input.txt', 'r')

def dfs(num, dir):
    check[num] = 1
    if num < 3:
        if mag[num][2] != mag[num+1][6] and not check[num+1]:    # 자성 다를 경우
            dfs(num+1, -1*dir)              # 다음 자석 번호, 방향 반대
    if num > 0:
        if mag[num][6] != mag[num-1][2] and not check[num-1]:    # 자성 다를 경우
            dfs(num-1, -1*dir)              # 다음 자석 번호, 방향 반대

    if dir == 1:
        mag[num] = [mag[num].pop()] + mag[num]
    else:
        mag[num] = mag[num][1:] + [mag[num][0]]

# main
T = int(input())
for tc in range(1, T+1):
    K = int(input())
    mag = [list(map(int, input().split())) for _ in range(4)]
    for _ in range(K):      # K번 회전
        n, d = map(int, input().split())    # 자석 번호, 회전 방향
        check = [0] * 4
        dfs(n-1, d)

    result = 0
    for i in range(4):
        result += mag[i][0] * 2 ** i
    print("#{} {}".format(tc, result))