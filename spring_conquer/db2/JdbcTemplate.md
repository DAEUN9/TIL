### 스프링 JdbcTemplate

- JdbcTemplate 소개와 설정

  - 장점

    - `spring-jdbc` 라이브러리에 포함되어 있음
      - 스프링으로 JDBC를 사용할 때 기본으로 사용되는 라이브러리
      - 별도의 복잡한 설정 없이 바로 사용 가능
    - 반복 문제 해결
      - 템플릿 콜백 패턴을 사용해서, JDBC를 직접 사용할 때 발생하는 대부분의 반복 작업을 대신 처리
      - 개발자는 SQL을 작성하고, 전달할 파라미터를 정의하고, 응답 값을 매핑해 주기만 하면됨
      - 종류
        - 커넥션 획득
        - `statement`를 준비하고 실행
        - 결과를 반복하도록 루프를 실행
        - 커넥션 종료, `statement`, `resultset` 종료
        - 트랜잭션 다루기 위한 커넥션 동기화
        - 예외 발생시 스프링 예외 변환기 실행

  - 단점

    - 동적 SQL을 해결하기 어렵다

  - `build.gradle` 추가

    ```
    implementation 'org.springframework.boot:spring-boot-starter-jdbc'
    ```

    

