# 김다은

def solution(N, number):
    dp = [[] for i in range(9)]  # 9개까지 리스트

    for i in range(1, 9):  # N이 i번 쓰인경우
        dp[i].append(int(str(N) * (i)))  # 단일 수들 삽입

        for j in range(1, i):
            for x in dp[j]:  # N이 j번 쓰인 경우의 수와
                for y in dp[i - j]:  # N이 i-j번 쓰인 경우의 사칙연산
                    dp[i].append(x + y)
                    dp[i].append(x - y)
                    dp[i].append(x * y)
                    if y != 0:
                        dp[i].append(x // y)

        if number in dp[i]:
            return i  # i번째 쓰인경우에 number가 있으면 i리턴

    return -1  # 8개의 리스트 안에 number없으면 -1리턴