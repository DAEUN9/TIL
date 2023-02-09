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



- **기본 키 매핑**
  - 직접 할당 : `@Id`만 사용
  - 자동 생성 : `@GeneratedValue`
    - `AUTO` : DB에 맞춰서 자동 생성
    - `IDENTITY` : DB에 위임, MySQL
      - `em.persist()` 시점에 즉시 INSERT SQL 실행
      - AUTO_INCREMENT는 INSERT SQL을 실행하고 ID 값을 알 수 있음
    - `SEQUENCE` : DB 시퀀스 오브젝트 적용(순서로 생성)
      - `@SequenceGenerator` 로 특정 테이블 매핑가능
      - 버퍼링 방식 가능
      - 미리 개수를 확보할 수 있음
    - `TABLE` : 키 생성 전용 테이블로 DB 시퀀스를 흉내냄
      - 모든 DB에 다 적용 가능
      - 단점은 성능
      - `@TableGenerator`
  - 권장 식별자 전략
    - 기본 키 제약 조건 : null 아님, 유일, 변하면 안됨
    - 미래까지 이 조건을 만족하는 자연키 찾기 어려움
      - 대체키(비즈니스와 상관없는)를 찾자
    - 권장: Long형 + 대체키(uuid 등) + 키 생성 전략 사용



- **실전 예제**
  - 컬럼명 형식은 회사마다 다름
  - 데이터 중심 설계의 문제점
    - 현재 방식은 객체 설계를 테이블 설계에 맞춤
    - 테이블의 외래키를 객체에 그대로 가져옴
    - 객체 그래프 탐색 불가능
    - 참조가 없으므로 UML도 잘못됨