# 함수1

#### 1. Bulit-in 함수

```
['ArithmeticError',
 'AssertionError',
 'AttributeError',
 'BaseException',
 'BlockingIOError',
 'BrokenPipeError',
 'BufferError',
 'BytesWarning',
 'ChildProcessError',
 'ConnectionAbortedError',
 'ConnectionError',
 'ConnectionRefusedError',
 'ConnectionResetError',
 'DeprecationWarning',
 'EOFError',
 'Ellipsis',
 'EnvironmentError',
 'Exception',
 'False',] 
 # 등등
```

#### 2. 정중앙 문자

문자열의 길이가 짝수일 경우에는 정중앙 문자 2개 반환

```python
def get_middle_char(word):
    cnt = 1
    for i in word:
        cnt += 1
    if cnt%2 == 1:
        answer = word[cnt//2-1] + word[cnt//2]
    else:
        answer = word[cnt//2-1]
    return answer
```

#### 3. 위치 인자와 키워드 인자

오류가 발생하는 코드 고르기

```python
def ssafy(name, location='서울'):
    print(f'{name}의 지역은 {location}입니다.')

# (1)
ssafy('허준')

# (2)
ssafy(location='대전', name='철수')

# (3)
ssafy('영희', location='광주')

# (4)
ssafy(name='길동, '구미') # error
```

#### 4. 나의 반환값은

```python
def my_func(a,b):
    c = a + b
    print(c)

result = my_func(3,7)
print(result)
---------------------
result = None
```

#### 5. 가변 인자 리스트

평균 구하기

```python
def my_avg(*arg):
    avg = 0
    num = 0
    for i in arg:
        avg += i
        num += 1
    return avg/num
```

---

# 함수2

#### 1. List의 합 구하기

```python
def list_sum(l):
    sum = 0
    for i in l:
        sum = sum+i
    return sum
```

#### 2. Dictionary로 이루어진 List의 합 구하기

```python
def dict_list_sum(d):
    sum = 0
    for i in d:
        sum += i['age']
        
    return sum
```

#### 3. 2차원 List의 전체 합 구하기

```python
def all_list_sum(l):
    sum = 0
    for i in l:
        for j in i:
            sum += j
    return sum
```

---

# 함수3

#### 1. 이름 공간(Namespace)

변수를 찾을 때 접근하는 이름 공간을 순서대로 작성

```
* Local scope: 함수
* Enclosed scope: 특정 함수의 상위 함수 
* Global scope: 함수 밖의 변수 혹은 import된 모듈
* Built-in scope: 파이썬안에 내장되어 있는 함수 또는 속성
```

## 2. 매개변수와 인자, 그리고 반환

옳지않은 것

```
(1) 함수는 오직 하나의 객체만 반환할 수 있으므로 'return a, b'와 같이 쓸 수 없다.
# error
튜플로 반환된다
```

## 3. 재귀 함수

```
* 장점
재귀함수는 반복문에 비해
코드가 직관적이고 이해하기 쉬움
코드 재사용이 쉬움

* 단점
메모리 스택이 넘치거나
프로그램 실행 속도가 늘어지는 단점이 있음
```

---

# 함수4

#### 1. 숫자의 의미

각 정수에 대응되는 아스키 문자를 이어붙인 문자열을 반환하는 메서드 작성

```python
def get_secret_word(*args):
    string = ''
    for i in args[0]:
        string += chr(i)
    return string

get_secret_word([83, 115, 65, 102, 89])
```

#### 2. 내 이름은 몇일까?

각 문자에 대응되는 아스키 숫자들의 합 반환

```python
def get_secret_number(a):
    num = 0
    for i in a:
        num += ord(i)
    return num

get_secret_number('tom')
```

#### 3. 강한 이름

문자열 2개를 전달 받아 각 문자열에 대응되는 아스키 숫자들의 합을 비교하여 더 큰 값 문자열 반환

```python
def get_strong_word(a,b):
    num1, num2 = 0, 0
    for i in a:
        num1 += ord(i)
    for j in b:
        num2 += ord(j)
    return (num1 if num1>=num2 else num2)

get_strong_word('z', 'a')
get_strong_word('tom','john')
```