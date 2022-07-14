# 폰켓몬
# <해시>
# https://school.programmers.co.kr/learn/courses/30/lessons/1845?language=python3

def solution(nums):
    # 포켓몬 종류: 수
    d = dict()

    # 뽑을 포켓몬 수
    N = len(nums)//2

    # 포켓몬 수 구하기
    for num in nums:
        d[num] = d.get(num, 0) + 1

    # 최대 포켓몬 수 구하기
    return min(N, len(d))