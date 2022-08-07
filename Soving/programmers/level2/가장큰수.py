# 가장큰수
# 정렬
# https://school.programmers.co.kr/learn/courses/30/lessons/42746
def solution(numbers):
    numbers = list(map(str, numbers))
    # 문자열에 3을 곱하여 문자열을 3개씩 반복
    # 원소 값이 1000이하이므로 3자리
    # 34>3>32
    numbers.sort(key = lambda x: x*3, reverse=True)
    # 000일때 처리를 위해 int로 바꿔줌
    return str(int(''.join(numbers)))