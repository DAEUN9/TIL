import sys
import time
start = time.time()
sys.stdin = open('input.txt', 'r')

K = int(input())


# 소인수 분해 최적화(logN)
def prime(k):
    x = k
    arr = []  # 소인수분해를 담을 리스트
    for i in range(2, k):
        if i * i > k:  # O(LogN)까지만 실행
            break

        while x % i == 0:  # 해당 i로 나누어진다면
            arr.append(i)  # 그 i를 넣어주고
            x //= i  # 계속 나눠준다.
    if x != 1:  # 만약 나눠지지 않은 소수가 있다면
        arr.append(x)  # 마지막 남은 소수를 추가해준다.
    return arr


# 정답을 출력할 리스트
answer = []

# 1. 첫번째 서리 처리
arr = prime(K)  # 가장 처음 소인수 분해를 한다.
if len(arr) == 1:  # 그 길이가 1이면
    K -= 1  # -1 해주고(최대 무게를 구해야하기 때문에)
    arr = prime(K)  # 한번더 해당 무게로 소인수분해를 한다.

# 2. 두번째 서리이후 처리
while True:
    K = sum(arr)  # 전에 훔쳤던 양의 합 설정
    arr = prime(K)  # 해당 무게로 소인수 분해 실행.
    answer.append(K)  # 훔친 양을 저장
    if len(arr) == 1:  # 만약 더이상 훔치지 않는다면(즉, 훔칠 수 있는 수박이 한개라면)
        break  # 탈출

answer.sort()  # 오름차순 정렬
print("time :", time.time() - start)
print(*answer)  # 정답 출력