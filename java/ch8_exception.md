# 예외처리

### 프로그램 오류

- 컴파일 에러
- 런타임 에러
- 논리적 에러: 실행은 되지만 의도 와 다르게 동작
- 예외: 다소 미약한 오류



### 예외 클래스의 계층구조

- 모든 예외의 최고 조상은 Exception

- 두 그룹
  - Exception클래스와 그 자손들 : 사용자의 실수같은 외적인 요인
  - RuntimeException클래스와 그 자손들: 프로그래머의 실수



### 예외 처리하기- try-catch문

```java
try {
    // 예외가 발생할 가능성이 있는 문장들
} catch (Exception1 e1) {
    // Exception1이 발생했을 경우, 이를 처리하기 위한 문장
} catch (Exception2 e2) {
    // Exception2가 발생했을 경우, 이를 처리하기 위한 문장
}
```

- 단 하나의 catch문만 실행



### printStackTrace()와 getMessage()

- printStackTrace(): 예외발생 당시의 호출스텍에 있었던 메서드의 정보와 예외 메시지를 화면에 출력
  - `참조변수.printStackTrace()`
- getMessage(): 발생한 예외클래스의 인스턴스에 저장된 메시지를 얻을 수 있음
  - `참조변수.getMessage()`



### 멀티 catch블럭

- `|`기호를 이용해서, 하나의 catch블럭으로 합칠 수 있음

```java
try {
    ...
} catch (ExceptionA | ExceptionB e){
    e.printStackTrace();
}
```

- 두 예외클래스가 조상과 자손이면 컴파일 에러



### 예외 발생시키기

1. 예외 클래스 객체 생성
   - `Exception e = new Exception();`
2. 키워드 throw를 이용 예외 발생
   - `throw e;`



###  checked예외, unchecked예외

- RuntimeException클래스와 그 자손은 프로그래머 실수기 때문에 예외처리 강제 x



### 메서드에 예외 선언

```java
void method() throws Exception1, Exception2, ... ExceptionN {
    // 메서드의 내용
}
```



### finally 블럭

```java
try {
    // 예외가 발생할 가능성이 있는 문장
} catch (Exception1 e1) {
    // 예외처리를 위한 문장
} finally {
    // 예외의 발생여부에 관계없이 항상 수행되어야하는 문장들
    // finally 블럭은 try-catch 맨 마지막에 위치
}
```



### 연결된 예외

- 예외 A가 예외 B를 발생시킬 수 있다
- 과정
  1. 예외 생성
  2. `initCause()`로 원인 예외 등록
- `initCause()`: 지정한 예외릘 원인 예외로 등록
- `getCause()`: 원인 예외를 반환
- 이렇게하면 두 예외가 상속아 아니어도 묶을 수 있음
- 다른 이유는 checked예외를 unchecked예외로 바꿀 수 있음