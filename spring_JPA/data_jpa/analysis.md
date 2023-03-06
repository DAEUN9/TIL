## 스프링 데이터 JPA 분석

- 스프링 데이터 JPA 구현체 분석

  - `org.springframework.data.jpa.repository.support.SimpleJpaRepository`

    ```java
    @Repository
    @Transactional(readOnly = true)
    public class SimpleJpaRepository<T, ID> ...{
        
        @Transactional
        public <S extends T> S save(S entity) {
            
            if (entityInformation.isNew(entity)) {
                em.persist(entity);
                return entity;
            } else {
                return em.merge(entity);
            }
        }
        ...
    }
    ```

    - `@Repository` 적용: JPA 예외를 스프링이 추상화한 예외로 변환
    - `@Transactional` 트랜잭션 적용
      - JPA의 모든 변경은 트랜잭션 안에서 동작
      - 스프링 데이터 JPA는 변경(등록, 수정, 삭제) 메서드를 트랜잭션 처리
      - 서비스 계층에서 트랜잭션을 시작하지 않으면 리파지토리에서 트랜잭션 시작
      - 서비스 계층에서 트랜잭션을 시작하면 리파지토리는 해당 트랜잭션을 전파 받아서 사용
      - 그래서 스프링 데이터 JPA를 사용할 때 트랜잭션이 없어도 데이터 등록, 변경이 가능했음
        - 사실은 트랜잭션이 리포지토리 계층에 걸려있는 것임
    - `@Transactional(readOnly = true)`
      - 플러시를 생략해서 약간의 성능 향상을 얻을 수 있음
    - **`save()` 메서드**
      - 새로운 엔티티면 저장( `persist` )
      - 새로운 엔티티가 아니면 병합( `merge` )
      - 가급적 merge는 사용하지 말자
    - `merge()`
      - 준영속 상태의 엔티티를 영속 상태로 만드는 기능
      - 복사된 엔티티가 서로 다른 객체가 되어 버리기 때문에, 영속성 컨텍스트 내에서 불일치성이 발생할 수 있음
      - merge() 메소드 대신 엔티티를 조회한 후 변경 내용을 바로 업데이트하는 방법을 사용하는 것이 좋음



- 새로운 엔티티를 구별하는 방법

  - 새로운 엔티티를 판단하는 기본 전략

    - 식별자가 객체일 때 `null` 로 판단
    - 식별자가 자바 기본 타입일 때 `0` 으로 판단
    - `Persistable` 인터페이스를 구현해서 판단 로직 변경 가능

  - `Persistable`

    ```java
    package org.springframework.data.domain;
    
    public interface Persistable<ID> {
        ID getId();
        boolean isNew();
    }
    ```

  - `Persistable` 구현

    ```java
    @Entity
    @EntityListeners(AuditingEntityListener.class)
    @NoArgsConstructor(access = AccessLevel.PROTECTED)
    public class Item implements Persistable<String> {
        
        @Id
        private String id;
        
        @CreatedDate
        private LocalDateTime createdDate;
        public Item(String id) {
            this.id = id;
        }
        
        @Override
        public String getId() {
            return id;
        }
        
        @Override
        public boolean isNew() {
            return createdDate == null;
        }
    }
    ```

  - 참고
    - JPA 식별자 생성 전략이 `@GenerateValue` 면 `save()` 호출 시점에 식별자가 없으므로 새로운 엔티티로 인식해서 정상 동작
    - `@Id` 만 사용해서 직접 할당이면 이미 식별자 값이 있는 상태로 `save()` 를 호출
      - `merge()` 호출됨
    - `Persistable`을 사용해서 새로운 엔티티 확인 여부를 직접 구현하면 효과적
    - 등록시간을 조합해서 사용하면 새로운 엔티티 여부를 편리하게 확인 가능
      - 등록 시간이 없으면 새로운 엔티티로 판단