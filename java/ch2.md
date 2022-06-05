# Java 기초 1



### 변수의 타입

- int
- long
  - 20억 넘을 때
- float
- double
  - 15자리
- char
- String



### 상수와 리터럴

- 상수는 변수와 달리 저장하면 변경 불가
- `final int MAX_VALUE = 10;`
- fianl을 앞에 붙여줌
- 모두 대문자로 하는게 관례 여러단어면 `_`로 구분



- 리터럴 : 그 자체로 값(기존 상수의 다른 이름)
- 리터럴 접미사
  - 논리형 - 없음
  - 정수형 - `L`(롱타입)
    - 중간에 구분자 넣을 수 있음 - `100_000_000_000L`
  - 실수형 - `f`(생략 불가), `d`(생략 가능) / float, double
  - 문자형 - 없음
  - 문자열 - 없음





### 문자 리터럴과 문자열 리터럴

- char 타입은 `'` `"` 사용
  - `'`은 빈문자열 허용 안함
- String 타입 `"` 사용
  - 빈 문자열 허용
- String 두가지 표현
  - `String name = new String("java");` - String 객체를 생성
  - `String name = "java";` - 위의 문장을 간단히



### 문자열 결합

- 문자열 + any type -> 문자열 + 문자열 => 문자열
- 7 + 7 + "" -> 14 + "" -> "14" + "" => "14"



### 기본형의 종류와 범위

- 논리형, 문자형, 정수형(int), 실수형(double)

| 종류/크기 | 1byte   | 2byte | 4byte   | 8byte      |
| --------- | ------- | ----- | ------- | ---------- |
| 논리형    | boolean |       |         |            |
| 문자형    |         | char  |         |            |
| 정수형    | byte    | short | **int** | long       |
| 실수형    |         |       | float   | **double** |



### printf를 이용한 출력

- 지시자를 통해 변수의 값을 여러 형식으로 변환하여 출력 가능
- 지시자의 순서와 개수 일치해야 함
- 자주 쓰는 지시자
  - `%d` : 10진 정수 형식
  - `%x` : 16진 정수 형식
  - `%f` : 부동 소수점의 형식
  - `%c` : 문자로 출력
  - `%s` : 문자열로 출력



### 화면으로부터 입력받기

```java
import java.util.Scanner; // Scanner 클래스를 사용하기 위해 추가

Scanner scanner = new Scanner(System.in); // Scanner 클래스의 객체를 생성

String input = scanner.nextLine(); // 입력받은 내용을 input에 저장
int num = Integer.parseInt(input); // 입력받은 내용을 int타입의 값으로 변환

// 바로 int로 입력받기
int num = scanner.nextInt(); // 정수를 입력받아서 변수 num에 저장
```



### 정수형의 오버플로우

- 최대값 + 1 -> 최소값
- 최소값 - 1 -> 최대값



### 타입 간의 변환방법

- 숫자를 문자로 변환 - 숫자에 '0' 더한다
- 문자를 숫자로 변환 - 문자에서 '0'을 뺀다
- 숫자를 문자열로 변환 - 숫자에 빈 문자열 ("")을 더한다
- 문자열을 숫자로 변환 - `Integer.parseInt()` 또는 `Double.parseDouble()`을 사용한다
- 문자열을 문자로 변환 - charAt(0)을 사용한다
  - `"3".charAt(0) -> '3'`
- 문자를 문자열로 변환 - 빈 문자열("")을 더한다



### 연산자 결합규칙

- 산술 > 비교 > 논리 > 대입
- 단항(1) > 이항(2) > 삼항(3)

- 단항 연산자와 대입 연산자를 제외한 모든 연산의 진행방향은 왼쪽에서 오른쪽





### 형 변환 연산자

- `(타입)피연산자`
  - int(84.3); -> 84



### 자동 형변환

- `float f = 1234;` // float f = (float)1234; 에서 (float)가 생략
- 사칙연산자
  - 피연산자 모두 int인 경우, 연산결과도 int타입
  - 올바른 연산결과를 얻기 위해서는 두 피연산자 중 한 쪽을 실수형으로 형변환
- 큰 자료형의 값을 작은 자료형의 변수에 저장하려면 명시적으로 형변환 해야함



### 문자열 비교

- `==` 대신 `equals()` 사용
  - 대소문자 구분

- `equalsIgnoreCase()`는 대소문자 구분 x

- `boolean result = str.equals("abc");`



### switch문

- 순서
  1. 조건식 계산
  2. 조건식의 결과와 일치하는 case문으로 이동
  3. 이후의 문장들 수행
  4. break문이나 switch문의 끝을 만나면 switch문 전체를 빠져나감

```java
switch (조건식) {
    case 값1 :
        // 조건식의 결과가 값1과 같을 경우 수행될 문장들
        // ...
        break;
    case 값2 :
        //...
        break;	// switch문을 벗어난다
    // ...
    default :
        // 조건식의 결과와 일치하는 case문이 없을 때 수행될 문장들
        // ...
}
```

- 제약조건
  1. 조건식 결과는 정수 또는 문자열 이어야 함
  2. case문의 값은 정수 상수(문자 포함), 문자열만 가능하며, 중복되지 않아야 한다

```java
public static void main(String[] args) {
    int num, result;
    final int ONE = 1;
    ...
    switch(result) {
        case '1':		// OK. 문자 리터럴(정수 49와 동일)
        case ONE:		// OK. 정수 상수
        case "YES":		// OK. 문자열 리터럴. JDK 1.7부터 허용
        case num:		// 에러. 변수는 불가
        case 1.0:		// 에러. 실수도 불가
            ...
    }
}
```





### 임의의 정수만들기

- `Math.random()`
  - 0.0과 1.0 범위에 속하는 하나의 double값을 반환
