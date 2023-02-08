## 엔티티 매핑

- **객체와 테이블 매핑**

  - `@Entity` : JPA가 관리, 엔티티라 함
    - 기본 생성자 필수(파라미터가 없는 public 또는 protected)
    - final 클래스, enum, interface, inner 클래스 사용 X
    - 저장할 필드는 final 사용 X

  - `@Table` : 엔티티와 매핑할 테이블 지정



- **데이터베이스 스키마 자동 생성**
  - DDL을 애플리케이션 실행 시점에 자동 생성
  - 이렇게 생성된 DDL은 개발 단계에서만 사용
  - DB 방언을 활용해서 DB에 맞는 적절한 DDL 사용
  - DB 스키마 자동 생성 - 주의
    - 운영 장비에는 절대 `create`, `create-drop`, `update` 사용하면 안됨
  - DDL 생성 기능
    - 제약 조건 추가
    - 유니크 제약 조건 추가
    - DDL을 자동 생성할 때만 사용되고 JPA 실행 로직에는 영향을주지 않음



- **필드와 컬럼 매핑**
  - `@Column` : DB 컬럼명 지정 가능
    - `name`, `nullable`, `unique` ...
    - unique제약조건을 달면 이름이 어려움
      - `@Table` 에서 유니크 조건 달기
  - `@Enumerated` : Enum타입 사용
    - `ORDINAL` : enum 순서를 DB에 저장
    - `STRING` : enum 이름을 DB에 저장
    - `ORDINAL`은 순서가 바뀌면 오류가 나기 쉬우므로 `STRING` 으로 쓰자
  - `@Temporal` : DATE, TIME, TIMESTAMP(DATE_TIME)
  - `@Lob` : DB에 큰 컨텐츠를 넣고 싶으면 사용
  - `@Transient` : 객체 데이터와 테이블 컬럼의 매핑 관계 제외
- **기본 키 매칭**