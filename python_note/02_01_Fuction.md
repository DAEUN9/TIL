# 함수

### 함수

> 특정한 기능(function)을 하는 코드의 묶음





### 함수를 쓰는 이유

- 가독성
- 재사용성
- 유지보수





### 내장함수(Built - in Functions)

<center>
    <img src="https://user-images.githubusercontent.com/18046097/61181739-2984fd80-a665-11e9-991b-f2f058397a69.png", alt="built_in">
</center>




### 매개변수(parameter) & 전달인자(argument)

```python
# 매개변수
입력을 받아 함수 내부에서 활용할 변수
함수를 정의하는 부분에서 확인 가능
	def fuc(x):
		return x + 2
	# x는 매개변수
	
# 전달인자
실제로 전달되는 값
함수를 호출하는 부분에서 볼 수 있음
func(2)
```





#### 기본 인자 & 키워드 인자

```python
# 기본 인자
입력된 값이 없을 때, 그 상황에서 사용할 값
	def 함수이름(이름='입력이 없으면 사용할 값'):
    	매개변수를 활용하여 문장(문자열)을 완성하여 리턴합니다.
    	
# 키워드 인자
함수를 호출할 때 키워드 인자를 활용하여 직접 변수의 이름으로 특정 인자 전달 가능
위치 인자와 함께 사용 가능
	greeting(name='철수', age=24)
	# 위치가 바뀌어도 됨
```





#### 가변(임의) 인자 리스트(Arbitrary Argument Lists)

- 개수가 정해지지 않은 임의의 인자를 받기 위해서 함수를 정의할 때 사용
- tubple 형태로 처리, 매개변수에 * 로 표현
- 매개변수 목록의 마지막에 옴

```python
def func(a, b, *args):
```





#### 가변(임의) 키워드 인자(Arbitrary Keyword Arguments)

- dict 형태로 처리, 매개변수에 ** 로 표현

```python
def func(**kwargs):
# **kwargs: 임의의 개수의 키워드 인자를 받음을 의미

# 예시
	def my_dict(**kwargs):
    return kwargs

	print(my_dict(한국어='안녕', 영어='hi', 독일어='Guten Tag'))
	----------------------------------------------------------
	{'한국어': '안녕', '영어': 'hi', '독일어': 'Guten Tag'}
```





### 스코프(scope)

```python
# LEGB Rule
	아래와 같은 순서로 이름을 찾아 나감
- Local scope: 함수
- Enclosed scope: 특정 함수의 상위 함수
- Global scope: 함수 밖의 변수 혹은 import된 모듈
- Built-in scope: 파이썬안에 내장되어 있는 함수 또는 속성
	# 단, 함수 내에서 필요한 상위 스코프 변수는 인자로 넘겨서 활용 (클로저 제외)
```





#### 반복문과 재귀함수

```
재귀함수는 코드가 더 직관적이고 이해하기 쉬운 경우가 있다.
변수 사용을 줄여줄 수 있다.
하지만, 메모리 스택이 넘치거나 실행 속도가 늘어지는 단점이 생긴다.
```





#### 최대 재귀 깊이

```python
import sys
print(sys.getrecursionlimit())
# 파이썬에서는 최대 재귀 깊이가 1,000으로 정해져 있다.
```





### map(function, iterable)

```python
- 순회가능한 데이터 구조의 모든 요소에 fuction을 적용한 후 돌려줌
- return은 map_object형태
```





### filter(function, iterable)

```python
- iterable에서 fuction의 반환된 결과가 True 인 것들만 구성하여 반환
- filter object 를 반환
```





### zip(*iterables)

- 복수의 iterable 객체를 모아(zip())줌
- 결과는 튜플의 모음으로 구성된 zip object 를 반환

```python
# 예시
	li_2d = [
    [1, 3, 5],
    [7, 9, 11],
    [13, 15, 17],
    [19, 21, 23],
	]
	t_2d = list(zip(*li_2d))
	print(t_2d)
	-------------------------------------
	[(1, 7, 13, 19), (3, 9, 15, 21), (5, 11, 17, 23)]

# 예시2
    girls = ['jane', 'ashley', 'mary']
    boys = ['justin', 'eric', 'david']
    pair = list(zip(girls, boys))
    print(pair)
    -------------------------------------------------
    [('jane', 'justin'), ('ashley', 'eric'), ('mary', 'david')]
# *literable을 슬라이싱 가능
```





### lamda 함수

- 표현식을 계산한 결과 값을 반환
- 익명함수라고도 불림

```python
# 예시
	def triangle_area(b, h):
    return 0.5 * b * h
    # 같음
	lambda b, h: 0.5 * b * h
```

