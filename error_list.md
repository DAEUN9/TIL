# error_list



`TypeError: cannot unpack non-iterable int object`

 - 두 개의 변수에 하나의 값을 할당

`ValueError: too many values to unpack (expected 2)`

- 두 개의 변수에 세 개의 값을 할당

`TypeError: 'str' object is not callable`

- 예약어 변수할당 이후 사용

`ValueError: complex() arg is a malformed string`

- 공백 포함한 복소수 string 복소수로 변환할 때

`TypeError: 'str' object does not support item assignment`

- 문자열을 변경하려고 함

`TypeError: unsupported operand type(s) for +: 'int' and 'str'`

- 정수와 문자열 더하기

`ValueError: invalid literal for int() with base 10: '3.5'`

- float형 문자열 정수로 변환

`TypeError: unsupported operand type(s) for +: 'range' and 'range'`

- range끼리 더하기

`TypeError: unsupported operand type(s) for *: 'range' and 'int'`

- range를 연산자로 반복하려고함

`IndexError: string index out of range`

- 인덱스 범위를 초과하여 접근

`SyntaxError: non-default argument follows default argument`

- 기본인자를 위치인자보다 먼저 위치한 경우

`SyntaxError: positional argument follows keyword argument`

- 키워드인자를 위치인자보다 먼저 위치한 경우

`SyntaxError: expression cannot contain assignment, perhaps you meant "=="?`

- 식별자를 숫자로만 이루었을 때

`TypeError: 'str' object is not callable`

- 내장함수를 변수로 바꿔서 지정하고 내장함수를 사용하려 했을때

`RecursionError: maximum recursion depth exceeded while calling a Python object`

- 1000이상의 재귀 깊이 호출

`NameError: name 'c' is not defined`

- 함수내의 지역변수 c를 접근하려고 함

`SyntaxError: EOL while scanning string literal`

- 따옴표 오류

`SyntaxError: unexpected EOF while parsing`

- 괄호 닫기 오류

`ZeroDivisionError: division by zero`

- 0으로 나눔

`NameError: name 'abc' is not defined`

- 정의되지 않은 변수 abc 호출

`TypeError: unsupported operand type(s) for +: 'int' and 'str'`

- int형과 str형 더하려고 함

`TypeError: type str doesn't define __round__ method`

- 문자열에 round함수를 사용

`TypeError: sample() missing 1 required positional argument: 'k'`

- 함수 호출 과정에서 필수 매개변수가 누락

`TypeError: choice() takes 2 positional arguments but 3 were given`

- 매개변수가 초과해서 들어옴

`ValueError: invalid literal for int() with base 10: '3.5'`

- 자료형은 올바르나 값이 적절하지 않음

`ValueError: 3 is not in list`

- 존재하지 않는 value를 조회

`IndexError: list index out of range`

- 존재하지 않는 index로 조회

`KeyError: 'queen'`

- 존재하지 않는 키로 접근

`ModuleNotFoundError: No module named 'reque'`

- 존재하지 않는 모듈을 import

`ImportError: cannot import name 'sampl' from 'random' (C:\Users\DANI\AppData\Local\Programs\Python\Python39\lib\random.py)`

- 모듈은 존재하나 존재하지 않는 클래스/함수를 가져오는 경우

`KeyboardInterrupt: `

- 사용자가 임으로 실행 중단

`IndentationError: expected an indented block`

- 들여쓰기를 안 한 경우

`IndentationError: unexpected indent`

- 들여쓰기를 아무데나 한 경우

`TypeError: test() missing 1 required positional argument: 'self'`

- self가 있는 메서드를 빈 것으로 호출

`AttributeError: type object 'Person' has no attribute 'docstring'`

- 잘못된 속성(데이터)를 호출

`AttributeError: 'Person' object has no attribute '__age'`

- private member 속성을 외부 호출하려고 함

`TypeError: 'str' object is not callable`

- 변수이름과 메서드이름을 똑같이 사용함
