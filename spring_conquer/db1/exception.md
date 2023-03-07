## 자바 예외 이해

- 예외 계층

  ![image-20230307234414778](exception.assets/image-20230307234414778.png)

  - `Object` : 예외도 객체이다. 모든 객체의 최상위 부모는 `Object` 이므로 예외의 최상위 부모도 `Object` 이다
  - `Throwable` : 최상위 예외이다. 하위에 `Exception` 과 `Error` 가 있다.
  - `Error` : 메모리 부족이나 심각한 시스템 오류와 같이 애플리케이션에서 복구 불가능한 시스템 예외이다.  애플리케이션 개발자는 이 예외를 잡으려고 해서는 안된다
    - 상위 예외를 잡으면 하위까지 잡을 수 있음
      - `Throwable`예외를 잡으면 안됨
    - 언체크 예외
  - `Exception` : 체크 예외
    - 애플리케이션 로직에서 사용할 수 있는 실질적인 최상위 예외이다.
    - `Exception` 과 그 하위 예외는 모두 컴파일러가 체크하는 체크 예외
    - `RuntimeException` 은 예외
  - `RuntimeException` : 언체크 예외, 런타임 예외
    - 컴파일러가 체크 하지 않는 언체크 예외이다.
    - `RuntimeException` 과 그 자식 예외는 모두 언체크 예외이다



- 예외 기본 규칙
  - 예외는 폭탄 돌리기와 같다. 잡아서 처리하거나, 처리할 수 없으면 밖으로 던져야한다
  - 예외를 처리하지 못하고 계속 던지면 어떻게 될까?
    - 자바 ` main()` 쓰레드의 경우 예외 로그를 출력하면서 시스템이 종료
    - 웹 애플리케이션의 경우 WAS가 해당 예외를 받아서 처리
      - 주로 사용자에게 개발자가 지정한, 오류 페이지를 보여줌



- 체크 예외 기본 이해

  - `Exception` 과 그 하위 예외는 모두 컴파일러가 체크하는 체크 예외
  - `RuntimeException` 은 예외

  ```java
  static class MyCheckedException extends Exception {
      public MyCheckedException(String message) {
          super(message);
      }
  }
  ```

  - 체크 예외를 잡아서 처리하는 코드

    ```java
    try {
        repository.call();
    } catch (MyCheckedException e) {
        //예외 처리 로직
    }
    ```

    - `catch`는 해당 타입과 그 해당 타입을 모두 잡을 수 있음

  - 체크 예외를 밖으로 던지는 코드

    ```java
    public void callThrow() throws MyCheckedException {
        repository.call();
    }
    ```

    - `throws` 를 지정하지 않으면 컴파일 오류가 발생한다
    - 체크 예외의 경우 예외를 잡아서 처리하거나 또는 예외를 밖으로 던진다는 선언을 필수로 해주어야 한다.

  - 장점
    - 개발자가 실수로 예외를 누락하지 않도록 컴파일러를 통해 문제를 잡아주는 훌륭한 안전 장치이다
  - 단점
    - 번거로움
    - 크게 신경 쓰고 싶지 않은 예외까지 모두 챙겨야 함
    - 의존관계에 딸느 단점도 있음



- 언체크 예외 기본 이해

  - RuntimeException 과 그 하위 예외

  - 컴파일러가 예외를 체크하지 않는다는 뜻

  - 예외를 던지는 throws 를 선언하지 않고,  생략할 수 있다

    - 자동으로 예외를 던짐

  - 언체크 예외를 밖으로 던지는 코드 - 생략

    ```java
    public void callThrow() {
        repository.call();
    }
    ```

    - 언체크 예외는 체크 예외와 다르게 `throws` 예외 를 선언하지 않아도 된다
    - 말 그대로 컴파일러가 이런 부분을 체크하지 않기 때문에 언체크 예외이다.
    - 참고로 언체크 예외도 `throws` 예외 를 선언해도 된다.

  - 장점

    - 신경쓰고 싶지 않은 언체크 예외를 무시할 수 있다
    - 의존관계를 참조하지 않아도 되는 장점이 있음

  - 단점

    - 개발자가 실수로 예외를 누락할 수 있다



- 체크 예외 활용

