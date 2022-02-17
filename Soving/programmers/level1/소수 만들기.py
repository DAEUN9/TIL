from itertools import combinations


def check(li):
    total = sum(li)
    for i in range(2, total):
        if total % i == 0:
            return False
    return True


def solution(nums):
    answer = 0
    A = list(combinations(nums, 3))
    for j in A:
        if check(list(j)) == True:
            answer += 1
    return answer
a= solution([1, 2, 3, 4, 5])
print(a)