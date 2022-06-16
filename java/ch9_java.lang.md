# Java.lang패키지와 유용한 클래스



### Object클래스의 메서드 - equals()

- 두 객체를 비교
- boolean
- `a.equals(b)`



### equals()의 오버라이딩

- value인스턴스가 가지고 있는 value값을 비교하는 법
- Value클래스에서 equals메서드를 오버라이딩하여 주소가 아닌 객체에 저장된 내용을 비교



### Object클래스의 메서드 -hashCode()

- 객체의 주소값을 이용해 해시코드를 만들어 반환
- 문자열 내용이 같으면 동일한 해시코드 값
  - `객체.hashCode()`
- 반면 `System.identifyHashCode(변수)`는 항상 다른 해시값



### Object클래스의 메서드 - toString()

- 인스턴스 변수에 저장된 값들을 문자열로 표현
- `객체.toString()`



### toStrint()의 오버라이딩

- 일반적으로 인스턴스나 클래스에 대한 정보 또는 인스턴스 변수들의 값을 문자열로 변환하여 반환하도록 오버라이딩



### String 클래스

- 변경 불가능
- 연산마다 새로운 문자열이 만들어짐
- 결합이나 추출이 많이 필요한 경우는 StringBuffer클래스 사용 권장(변경가능)



### 문자열의 비교

- 문자열 생성방법
  - 문자열 리터럴 저장: `String str1 = "abc";`
    - 이미 존재하는것 재사용
    - 같은 값은 같은 String인스턴스 참조
  - String클래스의 생성자를 사용: `String str2 = new String("abc")`
    - 항상 새로운 String인스턴스 생성



### 빈 문자열

```java
char[] chArr = new char[0];	// 길이가 0인 char배열
int[] iArr = {};			// 길이가 0인 int배열
```

```java
String s = "";	// 빈 문자열로 초기화
char c = ' ';	// 공백으로 초기화
```

- char형 변수에는 반드시 하나의 문자를 지정



### String클래스의 생성자와 메서드📚



### join()과 StringJoiner

- 여러 문자열 사이에 구분자를 넣어서 결합
- `String str = String.joins("-", arr);`



### 문자열과 기본형 간의 변환

- 기본형 -> 문자열
  - `String String.valueOf(타입 변수)`
- 문자열 -> 기본형
  - `타입 타입.pasrse타입(String 변수)`



### StringBuffer의 생성자

- 버퍼의 크기를 지정해주지 않으면 16개의 문자를 저장할 수 있는 크기의 버퍼 생성



### StringBuffer의 비교

- equals메서드를 오버라이딩하지 않아서 StringBuffer클래스의 equals메서드를 사용해도 `==`로 비교한 것과 같은 결과
- 반면 toString()은 오버라이딩 되어있음



### StringBuffer의 생성자와 메서드📚



### StringBuilder

- StringBuffer에서 쓰레드의 동기화만 뺌
- StringBuffer와 완전히 똑같은 기능이라 StringBuilder로 바꾸기만하면 됨



### Math클래스

- 생성자는 접근 제어자가 private
- Math클래스의 메서드는 모두 static
- Math의 메서드📚



### 래퍼 클래스

- 기본형 변수도 어쩔 수 없이 객체로 다뤄야 하는 경우 있음
- 종류
  - Boolean
  - Character
  - Byte
  - Short
  - Integer
  - Long
  - Float
  - Double



### Number클래스

- 기본형 중 숫자와 관련된 래퍼 클래스들은 모두 Number클래스의 자손



### 문자열을 숫자로 변환하기

- 문자열 -> 기본형
  - `타입 변수 = 타입.parse타입(문자열)`
- 문자열 -> 래퍼 클래스
  - `타입 변수 = 타입.valueOf(문자열)`



### 오토박싱 & 언박싱

- 기본형과 참조형 간의 덧셈 가능
- 오토박싱: 기본형 값을 래퍼 클래스의 객체로 자동 변환
- 언박싱: 래퍼클래스의 객체를 기본형 값으로 변환