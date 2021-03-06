# Array

### 알고리즘

> 어떠한 문제를 해결하기 위한 절차

- 표현 방법 크게 두 가지
  - 의사코드(슈도코드)
  - 순서도

- 좋은 알고리즘
  - 정확성
  - 작업량: 시간 복잡도로 표현
  - 메모리 사용량
  - 단순성
  - 최적성
- 시간 복잡도(빅-오 표기법)
  - 시간 복잡도 함수 중 가장 큰 영향력을 주는 n에 대한 항 표시
  - 계수는 생략하여 표시



### 배열

> 일정한 자료형의 변수들을 하나의 이름으로 열거하여 사용



### 정렬

- 대표정렬
  - 버블 정렬, 카운팅 정렬, 선택 정렬, 퀵 정렬, 삽입 정렬, 병합 정렬



### 버블 정렬(Bubble Sort)

> 인접한 두 개의 원소를 비교하여 자리를 계속 교환
>
> O(n^2)

- 정렬과정
  - 첫 번째 원소부터 인접 원소끼리 계속 자리를 교환하면서 맨 마지막 자리까지 이동
  - 한 단계가 끝나면 가장 큰 원소가 마지막 자리로 정렬
  - 교환하며 자리를 이동하는 모습이 거품 모양 비슷

```
# 의사 코드
BubbleSort(a, N)					# 정렬할 배열과 배열의 크기
	for i : N-1 -> 1				# 정렬될 구간의 끝
		for j : 0 -> i-1			# 비교할 원소 중 왼쪽 원소의 인덱스
			if a[j] > a[j+1]		# 왼쪽 원소가 더 크면
				a[j] <-> a[j+1]		# 오른쪽 원소와 교환
```

```python
def BubbleSort(a, N): # 정렬할 List, N 원소 수
    for i in range(N-1, 0, -1):
        for j in range(0, i)
        	if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
```





### 카운팅 정렬(Counting Sort)

> 항목들의 순서를 결정하기 위해 집합에 각 항목이 몇 개씩 있는지 세는 작업, 선형 시간에 정렬
>
> O(n+k): n은 리스트 길이, k는 정수의 최대값

- 제한 사항
  - 정수나 정수로 표현될 수 있는 자료에 대해서만 적용 가능
  - 집합 내의 가장 큰 정수를 알아야 한다.

```
# 예시

DATA = [0, 4, 1, 3, 1, 2, 4, 1] # 원래 데이터
COUNTS = [0, 0, 0, 0, 0] # 발생 회수 담을 리스트

# COUNTS[0] = 0의 발생 회수
COUNTS = [1, 3, 1, 1, 2]

# 누적합으로 COUNTS 리스트 변환
COUNTS = [1, 4, 5, 6, 8]
# 가장 뒤에 위치한 값의 index가 저장됐다고 볼 수 있음

DATA[-1]부터 순회
COUNTS[DATA[-1]] 값 1 감소
새로운 리스트 TEMP의 인덱스를 COUNTS[DATA[-1]]로 하여 삽입
# DATA[0]까지 반복

TEMP = [0, 1, 1, 1, 2, 3, 4, 4]
# 완료
```

```python
def Counting_sort(A, B, k)
# A [] -- 입력 배열(1 to k)
# B [] -- 정렬된 배열
# C [] -- 카운트 배열

	C = [0] * (k+1)
    
    for i in range(0, len(A)):
        C[A[i]] += 1
        
    for i in range(1, len(C)):
        C[i] += C[i-1]
        
    for i in range(len(B)-1, -1, -1):
        C[A[i]] -= 1
        B[C[A[i]]] = A[i]
```



### 정렬 알고리즘 비교

![3](https://hoyeonkim795.github.io/assets/img/sort_algorithm/3.png)



### 완전 검색(Exaustive Search)

> 모든 경우의 수 나열하고 확인
>
> Brute-force 혹은 generate-and-test기법 이라고도 불리운다.



#### 순열 (Permutation)

- {1,2,3}을 포함하는 모든 순열을 생성하는 함수

  ```python
  for i1 in range(1, 4):
      for i2 in range(1, 4):
          if i2 != i1:
              for i3 in range(1, 4):
                  if i3 != i1 and i3 != i2:
                      print(i1, i2, i3)
  ```





### 탐욕(Greedy) 알고리즘

> 최적해를 구하는 데 사용되는 근시안적인 방법
>
> 그 순간에 최적이라고 생각되는 것을 선택해나감
>
> 지역적으로 최적, 최종 해답이 최적이라는 보장 X

- 동작 과정

  1. **해 선택**: 부분 문제의 최적 해를 구한 뒤, 부분해 집합에 추가

  2. **실행 가능성 검사**: 새로운 부분해 집합이 실행 가능한지 확인

     (문제의 제약 조건을 위반하지 않는지 검사)

  3. **해 검사**: 새로운 부분해 집합이 문제의 해가 되는지 확인

     아직 전체 문제의 해가 완성되지 않았다면 1번 부터 다시 시작.

````
# 거스름돈 줄이기 예시

1. 가장 단위가 큰 동전을 하나 골라 거스름돈에 추가
2. 거스름돈이 손님에게 내드려야 할 액수를 초과하는지 확인
	초과한다면 마지막에 추가한 동전 빼고, 1번으로 돌아가 더 작은 동전 추가
3. 거스름돈과 손님에게 내드려야 하는 액수 일치하는지 확인, 모자라면 1번으로 돌아감
````

```
# Baby-gin
0~9 숫자 카드에서 임의의 카드 6장을 뽑았을 때,
3장의 카드가 연속적인 번호를 갖는 경우를 run
3장의 카드가 동일한 번호를 갖는 경우 triplet

6장의 카드가 run과 triplet로만 구성된 경우는 baby-gin
```

```python
# Baby-gin 코드
num = 456789 # Baby Gin 확인할 6자리 수
c = [0] * 12 # 6자리 수로부터 각 자리 수를 추출하여 개수를 누적할 리스트

for i in range(6):
    c[num%10] += 1
    num //= 10

i = 0
tri = run = 0
while i < 10:
    if c[i] >= 3: # triplete 조사 후 데이터 삭제
        c[i] -= 3
        tri += 1
        continue
    if c[i] >= 1 and c[i+1] >= 1 and c[i+2] >= 1: # run 조사 후 데이터 삭제
        c[i] -= 1
        c[i+1] -= 1
        c[i+2] -= 1
        run += 1
        continue
    i += 1
if run + tri == 2:
    print("Baby Gin")
else:
    print("Lose")
```

- 입력받은 숫자를 정렬한 후, 앞뒤 3자리씩 확인하는 방법 고려 가능
  - 예) [1, 2, 3, 1, 2, 3]
    - 정렬하면 [1, 1, 2, 2, 3, 3]으로 오히려 baby-gin 확인 실패할 수 있음
- 탐욕 알고리즘적인 접근은 해답을 찾아내지 못하는 경우도 있으니 유의!