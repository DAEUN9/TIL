# 에러 & 예외 처리

## 에러(Error)





### 문법 에러(Syntax Error)

- `SyntaxError: invalid syntax`: 콜론 누락 등 문법 오류
- `SyntaxError: EOL while scanning string literal`: 따옴표 오류
- `SyntaxError: unexpected EOF while parsing`: 괄호 닫기 오류





### 예외(Exception)

> 문법적으로는 옳지만, 실행 시 발생하는 에러
>
> 아래 제시된 모든 에러는 `Exception` 을 상속받아 이루어짐

- `ZeroDivisionError`: 어떤 수를 0으로 나누게 되면 발생하는 에러

- `NameError`: 정의되지 않은 변수를 호출하였을 경우 발생
- `TypeError`: 자료형이 올바르지 못한 경우
  - `TypeError: unsupported operand type(s) for +: 'int' and 'str'`: 숫자+문자
  - `TypeError: type str doesn't define __round__ method`: 문자에 round()
  - `TypeError: sample() missing 1 required positional argument: 'k'`: 함수 호출에서 필수 매개변수 누락
  - `TypeError: choice() takes 2 positional arguments but 3 were given`: 함수 호출에서 매개변수 개수 초과
- `ValueError`: 자료형은 올바르나 값이 적절하지 않음
  - `ValueError: invalid literal for int() with base 10: '3.5'`: 정수 아닌 값을 int()
  - `ValueError: 3 is not in list`: 리스트에 없는 값을 찾음
- `IndexError`: 존재하지 않는 index로 조회
- `KeyError`: 존재하지 않는 key로 접근
- `ModuleNotFoundError`: 존재하지 않는 Modeul을 `import `하는 경우
- `ImportError`: Module은 찾았으나 존재하지 않는 클래스/함수를 가져오는 경우
- `KeyboardInterrupt`: 사용자가 임의로 실행을 중단한 경우
- `IndentationError`: Indentation(들여 쓰기)이 적절하지 않은 경우





------------------

## 예외 처리(Exception Handling)





### `try` & `except`

- `try` 아래의 코드 블록이 실행
- 예외가 발생되지 않으면, `except` 없이 실행 종료
- 예외가 발생하면, 남은 부분을 수행하지 않고, `except` 가 실행

```python
# 활용법
try:
    <코드 블록 1>
except (예외):
    <코드 블록 2>
```

- 복수의 예외 처리 가능

  ```python
  # 활용법
  try:
      <코드 블록 1>
  except (예외 1, 예외 2):
      <코드 블록 2>
  
  # 활용법2
  try:
      <코드 블록 1>
  except 예외 1:
      <코드 블록 2>
  except 예외 2:
      <코드 블록 3>
  
  # 에러가 순차적으로 수행, 가장 작은 범주부터 시작해야 함.
  ```

#### `else`

- 에러가 발생하지 않는 경우 수행되는 문장은 `else` 이용
- 모든 `except` 절 뒤에 와야 함

```PYTHON
# 활용법
try:
    <코드 블럭 1>
except 예외:
    <코드 블럭 2>
else:
    <코드 블럭 3>
```

#### `finally`

- 반드시 수행해야 하는 문장
- 예외의 발생 여부와 관계없이 `try` 문을 떠날 때 항상 실행

```python
# 활용법
try:
    <코드 블럭 1>
except 예외:
    <코드 블럭 2>
finally:
    <코드 블럭 3>
```

#### 에러 메시지 처리 `as`

- `as` 키워드를 활용하여 에러 메시지를 보임

```python
# 활용법
try:
    <코드 블럭 1>
except 예외 as err:
    <코드 블럭 2>
    
# 예시
try:
    empty_list = []
    print(empty_list[-1])
except IndexError as err:
    print(f'{err}, 오류가 발생했습니다.')
--------------------------------------
list index out of range, 오류가 발생했습니다.
```





### 예외 발생 시키기(Exception Raising)

#### `raise`

- 예외를 강제로 발생

```python
# 활용법
raise <에러>('메시지')

# 예시
raise ValueError('hi')
---------------------
ValueError: hi
```

#### `assert`

- 상태를 검증하는데 사용
- 조건이 True이면 코드가 그대로 진행, False라면 `AssertionError` 발생

```python
# 활용법
assert Boolean expression, error message

# 예시
assert len([1, 2]) == 1, '길이가 1이 아닙니다.'
--------------------------------------------
AssertionError: 길이가 1이 아닙니다.
```

