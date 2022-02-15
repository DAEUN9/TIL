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
  ```

  

