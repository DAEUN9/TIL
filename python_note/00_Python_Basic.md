# Python 기초

### 변수(Variable)

```python
컴퓨터 메모리 어딘가에 저장되어 있는 객체를 참조하기 위해 사용되는 이름

- 객체(object): 값을 가지고 잇는 모든 것
- 동일 변수에 다른 객체를 언제든 할당 가능
```





### 식별자(Identifiers)

```python
변수, 함수 모듈, 클래스 등을 식별하는데 사용되는 이름
- 첫 글자에 숫자가 올 수 없다.
- 길이에 제한이 없다.
- 대/소문자(case)를 구분함
- 아래의 키워드는 사용할 수 없다
False, None, True, and, as, assert, async, await, break, class, continue, def, del, elif, else, except, finally, for, from, global, if, import, in, is, lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield
```





### 실수 비교하는 방법

```python
#1 abs(a - b)

#2 import sys
abs(a-b) <= sys.float_info.epsilon
# epsilon은 부동소수점 연산에서 반올림을 함으로써 발생하는 오차 상환

#3 import
math.inclose(a, b)
```





### 이스케이프 시퀀스(Escape sequence)

```python
\n : 줄바꿈
\t : 탭
\r : 캐리지리턴(커서를 행의 앞으로 이동)
\0 : 널(Null)
\\ : \
\' : 단일인용부호(')
\" : 이중인용부호(")
```





### String interpolation

```python
# %-formatting
'%s'%name	# 문자열
'%d'%score	# 정수
'%f'%score	# 실수 

# str.format()
'{}'.format(name)

# f-string
f'{pi:.3}'	# 3.14
# 여러줄 문자열에도 사용가능
# 출력 형식 지정 가능
# 연산 가능
```





### 딕셔너리(Dictionary)

```python
- key는 변경 불가능한 데이터만 가능
(string, integer, float, boolean, tuple, range)
- 중복된 key 존재 불가능
- 만드는 방법
#1 a = {'b':'되나'}
#2 a = dict(b='되나')

dic.keys() : key 목록
dic.values() : value 목록
dic.item() : key, value 목록

```





### 컨테이너형 형변환

![img](https://user-images.githubusercontent.com/18046097/61180466-a6a67780-a651-11e9-8c0a-adb9e1ee04de.png)





### 연산자 우선순위

```python
0. ()을 통한 grouping
1. Slicing
2. Indexing
3. 제곱연산자
    **
4. 단항연산자 
    +, - (음수/양수 부호)
5. 산술연산자
    *, /, %
6. 산술연산자
    +, -
7. 비교연산자, in, is
8. not
9. and
10. or
```





### 문장과 표현식의 관계

<center><img width="600" height="300" src="https://user-images.githubusercontent.com/9452521/87619771-f41f5e00-c757-11ea-9e4b-1f76e4ca0981.png", alt="variable"/></center>
