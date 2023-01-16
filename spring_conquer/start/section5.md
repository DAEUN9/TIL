## 스프링 DB 접근 기술

- 순수 JDBC
  - `DataSource` 필요 → 스프링에서 주입받음
  - `close` 해주어야 커넥션이 계속 쌓여 문제가 생기지 않음
- 스프링 통합 테스트
  - `@Transactional` : 테스트 후 데이터 롤백
  - 가급적 단위 테스트가 좋은 테스트일 경우가 많음

- 스프링 JdbcTemplate

  - `JDBC API` 에서 본 반복 코드를 대부분 제거해줌
  - SQL문은 직접 작성해야 한다.
  - `DataSource`를 `JdbcTemplate` 에 주입
    - 생성자가 한개면 `@Autowired`를 생략 가능
  - 디자인 패턴 중 템플릿 메서드 패턴이 많이 들어가 있음

- JPA

  - `application.properties`

    ```java
    spring.jpa.show-sql=true
    // create, update ...
    spring.jpa.hibernate.ddl-auto=none
    ```

  - 자바 진영의 표준 인터페이스

  - `ORM` : Object Relation Mapping

    - 데이터를 자동으로 매핑해줌

  - `IDENTITY` : DB가 알아서 생성해 주는 것

    - ex) `@GeneratedValue(strategy = GenerationType.IDENTITY)`

  - `EntityManager`  : 데이터소스를 들고있어서 DB통신 등을 내부적으로 처리

  - pk기반이 아닌 함수는 `JPQL`사용해야 함

  - 모든 데이터 변경이 트랜잭션 안에서 실행되야하기 때문에 `@Transactional` 필수

- 스프링 데이터 JPA

  - `JpaRepository<entity, pk>` 를 상속 받아야함
  - `JpaRepository` 를 상속받은 인터페이스를 자동으로 빈으로 등록해줌
  - 복잡한 동적 쿼리는 `Querydsl`이라는 라이브러리 사용