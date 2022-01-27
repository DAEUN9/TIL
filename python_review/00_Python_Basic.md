# 데이터

#### 1. Python 예약어(식별자)

```
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
```



#### 2. 실수 비교

실수표현에서 오차가 발생하여 연산 또는 비교가 되지 않을 때가 있다.

두 실수 값을 올바르게 비교하기 위한 코드

```python
num = 0.1 * 3
num2 = 0.3

print(abs(num-num2)<=1e-10)
```



#### 3. 이스케이프 시퀀스

(1) 줄 바꿈, (2) 탭, (3) 백슬래시

```
(1) 줄 바꿈: \n
(2) 탭: \t
(3) 백슬래시: \\
```



#### 4. String Interpolation

'안녕, 철수야'를 string interpolation으로 출력

```python
name = '철수'
print(f"'안녕, {name}야!'")
```



#### 5. 형 변환

오류가 발생하는 코드

```python
int('3.5') # float처럼 생긴 문자열을 int로 바로 못바꿈
```



#### 6. 네모 출력

n*m 직사각형 *로 출력, 반복문 사용 금지

```python
n = 5
m = 9

line = '*'*n
print(f'{line}\n'*m)
```



#### 7. 이스케이프 시퀀스 응용

print()함수 한번만 사용하여 다음 문장 출력

"파일은 c:\Windows\User\내문서\Python에 저장이 되었습니다."

나는 생각했다. 'cd를 써서 git bash로 들어가 봐야지.'

```python
print('\"파일은 c:\\Windows\\Users\\내문서\\Python에 저장이 되었습니다.\" 나는 생각했다.'+"'cd를 써서 git bash로 들어가 봐야지.\'")
```



#### 8. 근의 공식

```python
root1=((-1)*b+(b**2-4*a*c)**(1/2))/(2*a)
root2=((-1)*b-(b**2-4*a*c)**(1/2))/(2*a)
```

---

