### 변수와 식별자

- 카멜 케이스(myInfo)
  - 변수, 객체, 함수
- 파스칼 케이스
  - 클래스, 생성자에 사용
  - JS에서 사용 x
- 스네이크 케이스





#### 변수선언 키워드

- let
  - 재선언 x
  - 재할당 o

- const
  - 재선언 x
  - 재할당 x

- 블록 스코프
  - 중괄호 내부
  - 내부 변수는 밖에서 접근 불가능
- var
  - 호이스팅 문제
    - 변수를 선언 이전 참조할 수 있는 현상
    - 선언 이전의 위치에서 접근 시 `undefined`반환
  - 재선언 재할당 모두 가능
  - 사용x



### 데이터 타입

- 원시 타입

  - 객체x 기본 타입

  - 변수에 해당 타입의 값이 담김

  - 다른 변수에 복사할 때 실제 값이 복사

  - 숫자 타입

    - 정수, 실수 구분 없는 하나의 숫자
    - NaN: 연산 불가

  - 문자열 타입

    - 16비트 유니코드 문자 집합
    - 작은따옴표 큰따옴표 모두 가능
    - 

  - undefined

    - 값이 없음
    - 변수 선언 이후 값 할당 안하면 자동 undefined
    - 개발자 의도 x
    - typeof: `undefined`

  - null

    - 값이 없음 의도 o
    - typeof: `object`

    

- 참조 타입

  - 객체 타입 자료형
  - 변수에 해당 객체의 참조 값이 담김
  - 다른 변수에 복사할 때 참조 값이 복사



### 연산자

- 스타일가이드상 '+=, -=' 권장
- 알파벳은 아스키코드 값으로 비교
- 동등 비교 연산자(==)
  - 암묵적 타입 변환 o
- 일치 비교 연산자(===)
  - 엄격한 비교(타입과 값 모두 같은지)
  - 둘 다 객체인 경우 메모리에서 같은 값을 바라보는지
- 논리 연산자
  - &&
  - ||
  - !

- 삼항 연산자
  - 조건 참이면 `:`앞의 값 사용, 아니면 뒤의 값 사용
  - `조건 ? 값1 : 값2 `





### 조건문

- switch

  - break 없는 경우 밑의 case 모두 출력

  ```
  switch(변수) {
  case '변수': {
   ~~~
  	}
  ...
  default : {
  ~~~
  	}
  }
  ```

  



### 반복문

- while
- for
  - `for (initialization; condition; expression){}`
  - 최초 1회만 실행; 조건; 매 반복 시행 후 평가
- for ... in(딕셔너리)
  - 주로 객체의 속성(key)들을 순회
  - 배열 권장 x(인덱스 순 x)
  - 배열의 key값은 인덱스
- for ... of(배열)
  - 반복 가능한 객체 순회
  - Array, Map, Set, String ...



### 함수

- JS는 일급객체

  - 변수에 할당 가능
  - 함수의 매개변수로 전달 가능
  - 함수의 반환 값으로 사용 가능

- 함수 선언식

  - 함수의 이름과 함께 선언(익명함수 x)

  - 호이스팅 o

  - name, arg, 몸통 구성

    ```
    fuction name(args) {
    	// do something
    }
    ```

    

- 함수 표현식

  - 변수에 함수를 할당

  - 호이스팅 x

  - 함수의 이름 생략 가능(익명함수 o)

    ```
    const name = fuction (args) {
    	// do something
    }
    ```

- 기본인자 설정 가능
- 매개변수와 인자의 개수 불일치 허용
  - 적은 인자는 `undefined`
- rest parameter
  - 가변인자 리스트
  - `...args`
- spread operator
  - 언패킹



### Arrow Function

- function 키워드 생략 가능
- 함수의 매개변수 하나라면 `()`도 생략 가능
- 몸통이 표현식 하나라면 `{}` 와 `return` 생략 가능
- 기존 function 키워드 방식과 차이점 this

```javascript
// 1. function 키워드 삭제, 화살표 장착
const jegob = (a) => {
	return a * a
}

// 2. 매개변수가 한 개라면 소괄호 생략 가능
const jegob = a => {
    return a * a
}
// 매개 변수가 없으면?
// 괄호 생략 불가 => 빈 괄호나 언더스코어
const abc = _ => {
    return 'hi'
}

// 3. 코드 본문이 표현식 한 개인 경우 return, {} 생략
const jegob = a => a** 2

//
const divid = (a, b) => {
    if (b) {
        return a/b
    } else {
        return NaN
    }
}

const divid1 = (a,b) => b ? a/b : NaN
```





### 문자열

- includes
  - `string.includes(value)`
- split
  - `string.split(value)`
- replace
  - `string.replace(from, to)`
  - string.replaceAll(from, to)
- trim
  - `string.trim`
  - `string.trimStart()`
  - `string.trimEnd()`

##### MDN 문서 보기



### 배열

- 키 속성 - 참조 타입의 객체
- 순서 보장
- 대괄호 이용해 생성
- 배열 길이는 `array.length` 로 접근
- 0~ 양의 정수 인덱스로 접근 가능