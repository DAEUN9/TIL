### 2차원 배열

> 입력법

```python
# 1
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# 2
N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
```



### 배열 순회

- 행 우선 순회

  ```python
  # i 행의 좌표
  # j 열의 좌표
  
  for i in range(n):
      for j in range(m):
          Array[i][j]	# 필요한 연산 수행
  ```

- 열 우선 순회

  ```python
  # i 행의 좌표
  # j 열의 좌표
  
  for j in range(n):
      for i in range(m):
          Array[i][j]	# 필요한 연산 수행
  ```

- 지그재그 순회

​		------>

​		<-------

```python
# i 행의 좌표
# j 열의 좌표

for i in range(n):
    for j in range(m):
        Array[i][j + (m-1-2*j) * (i%2)]	
        # 필요한 연산 수행
```



### 델타를 이용한 2차 배열 탐색

- 2차 배열의 한 좌표에서 4방향의 인접 배열 요소 탐색

  ```python
  arr[0...N-1][0...N-1]	# N*N 배열
  di[] <- [0, 0, -1, 1]	# 상하좌우
  dj[] <- [-1, 1, 0, 0]
  for i : 1 -> N-1:
      for j : 1 -> N-1:
              for k in range(4):
                  ni <- i + di[k]
                  nj <- j + dj[k]
                  if 0<=ni<N and 0<=nj<N:	# 유효한 인덱스면
                      test(arr[ni][nj])
  ```

  

### zip을 이용한 전치행렬

```python
c = [[1,2,3], [4,5,6]]
print([list(x) for x in zip(*c)])
----------------------------------
[[1,4], [2,5], [3,6]]
```





### 부분집합

- 집합의 원소가 n개일 때, 공집합을 포함한 부분집합의 수는 2^n개

- loop문 부분집합 생성

  ```python
  bit - [0, 0, 0, 0]
  for i in range(2):
      bit[0] = i	# 0번째 원소
      for j in range(2):
          bit[1] = j	# 1번째 원소
          for k in range(2):
              bit[2] = k	# 2번째 원소
              for l in range(2):
                  bit[3] = l	# 3번째 원소
                  print_subset(bit)	# 생성된 부분집합 출력
  ```

  



### 비트 연산자

- `<<`
  - 1 << n: 2^n 즉, 원소가 n개일 경우 모든 부분집합 수
- `&`
  - i & (1<<j): i의 j번째 비트가 1인지 아닌지를 검사

- 부분집합 생성

  ```python
  arr = [3, 6, 7, 1, 5, 4]
  
  n = len(arr)	# n : 원소의 개수
  
  for i in range(1<<n):		# 1<<n : 부분 집합의 개수
      for j in range(n):		# 원소의 수만큼 비트를 비교함
          if i & (1<<j):		# i의 j번 비트가 1인 경우
              print(arr[j], end=', ')		# j번 원소 출력
      print()
  print()
  ```





### 이진 탐색(Binary Search)

- 자료가 정렬된 상태여야 한다.

- 검색 과정

  - 자료의 중앙에 있는 원소를 고른다

  - 중앙 원소의 값과 찾고자 하는 목표 값을 비교한다

  - 목표 값 < 중앙원소 -> 왼쪽 반에 대해 새로 검색

    목표 값 > 중앙원소 -> 오른쪽 반에 대해 새로 검색

  - 목표 값 찾을 때까지 반복

```python
def binarySearch(a, N, key)
	start = 0
    end = N-1
    while start <= end:
        middle = (start + end)//2
        if a[middle] == key:	# 검색 성공
            return true
        elif a[middle] > key:
            end = middle - 1
        else:
            start = middle + 1
    return false				# 검색 실패
```

- 재귀 함수 이용

  ```python
  def binarySearch2(a, low, high, key):
      if low > high:	# 검색 실패
          return False
      else:
          middle = (low + high) // 2
          if key == a[middle]:	# 검색 성공
              return True
          elif key < a[middle]:
              return binarySearch2(a, low, middle-1, key)
          elif a[middle] < key:
              return binarySearch2(a, middle+1, high, key)
  ```

  



### 인덱스

> 원본 데이터에 데이터가 삽입될 경우 상대적으로 크기가 작은 인덱스 배열을 정렬하기 때문에 속도가 빠름





### 선택 정렬(Selection Sort)

- 가장 작은 값의 원소부터 차례대로 선택하여 위치 교환

- 정렬 과정

  - 주어진 리스트 중에서 최소값 찾는다
  - 그 값을 리스트에 맨 앞에 위치한 값과 교환
  - 맨 처음 위치를 제외한 나머지 리스트를 대상으로 위의 과정 반복

- 알고리즘

  ```python
  def SelectionSort(a[], n)
  	for i from 0 to n-2
      	a[i], ..., a[n-1] 원소 중 최소값 a[k] 찾음
          a[i]와 a[k] 교환
  ```

- 선택 졍렬

  ```python
  def selectionSort(a, N):
      for i in range(N-1):
          minIdx = i
          for j in range(i+1, N):
              if a[minIdx] > a[j]:
                  minIdx = j
          a[i], a[minIdx] = a[minIdx], a[i]
  ```

  



### 셀렉션 알고리즘(Selection Algorithm)

- 저장되어 있는 자료로부터 k번째로 큰 혹은 작은 원소를 찾는 방법
- 선택 과정
  - 정렬 알고리즘을 이용해 자료 정렬
  - 원한는 순서에 있는 원소 가져오기

- k번째로 작은 원소를 찾는 알고리즘

  ```python
  def select(arr, k):
      for i in range(0, k):
          minIndex = i
          for j in range(i+1, len(arr)):
              if arr[minIndex] > arr[j]:
                  minIndex = j
          arr[i], arr[minIndex] = arr[minIndex], arr[i]
      return arr[k-1]
  ```

  