### API 개발 고급 - 지연 로딩과 조회 성능 최적화

- xToOne 성능 최적화

  - `OrderSimpleApiController`

    ```java
    /**
     *
     * xToOne(ManyToOne, OneToOne) 관계 최적화
     * Order
     * Order -> Member
     * Order -> Delivery
     *
     */
    @RestController
    @RequiredArgsConstructor
    public class OrderSimpleApiController {
        private final OrderRepository orderRepository;
        /**
     * V1. 엔티티 직접 노출
     * - Hibernate5Module 모듈 등록, LAZY=null 처리
     * - 양방향 관계 문제 발생 -> @JsonIgnore
     */
        @GetMapping("/api/v1/simple-orders")
        public List<Order> ordersV1() {
            List<Order> all = orderRepository.findAllByString(new OrderSearch());
            for (Order order : all) {
                order.getMember().getName(); //Lazy 강제 초기화
                // Member까지는 프록시 객체, name을 들고오려면 DB에 쿼리를 날려서 조회하게 됨
                order.getDelivery().getAddress(); //Lazy 강제 초기화
            }
            return all;
        }
    }
    ```

    - `order`을 `lazy` 초기화하지 않으면 오류 발생
      - 양방향 연관관계 문제
    - `order` -> `member` 와 `order` -> `address` 는 지연 로딩이다
      - 따라서 실제 엔티티 대신에 프록시 존재
    - `jackson` 라이브러리는 기본적으로 이 프록시 객체를 json으로 어떻게 생성해야 하는지 모름
    - `Hibernate5Module` 을 스프링 빈으로 등록하면 해결(스프링 부트 사용중)

  - 하이버네이트 모듈 등록

    - `implementation 'com.fasterxml.jackson.datatype:jackson-datatype-hibernate5'`

      - 스프링 부트 3.0 미만

    - 빈 등록

      ```java
      @Bean
      Hibernate5Module hibernate5Module() {
           //강제 지연 로딩 설정
       // 양방향 연관관계를 계속 로딩hibernate5Module.configure(Hibernate5Module.Feature.FORCE_LAZY_LOADING,true);
       return new Hibernate5Module();
      }
      ```

    -  초기화 된 프록시 객체만 노출, 초기화 되지 않은 프록시 객체는 노출 안함

  - 주의

    - 엔티티를 직접 노출할 때는 양방향 연관관계가 걸린 곳은 꼭! 한곳을 `@JsonIgnore` 처리
    - `Hibernate5Module` 를 사용하기 보다는 DTO로 변환해서 반환
    - 지연 로딩(LAZY)을 피하기 위해 즉시 로딩(EARGR)으로 설정하면 안된다
      - 성능 튜닝이 매우 어려워짐
      - 항상 지연 로딩을 기본으로 하고, 성능 최적화가 필요한 경우에는 페치 조인(fetch join)을 사용



- 엔티티를 DTO로 변환

  - `OrderSimpleApiController` - 추가

    ```java
    /**
     * V2. 엔티티를 조회해서 DTO로 변환(fetch join 사용X)
     * - 단점: 지연로딩으로 쿼리 N번 호출
     */
    @GetMapping("/api/v2/simple-orders")
    public List<SimpleOrderDto> ordersV2() {
        List<Order> orders = orderRepository.findAll();
        List<SimpleOrderDto> result = orders.stream()
            .map(o -> new SimpleOrderDto(o))
            .collect(toList());
        return result;
    }
    
    @Data
    static class SimpleOrderDto {
        private Long orderId;
        private String name;
        private LocalDateTime orderDate; //주문시간
        private OrderStatus orderStatus;
        private Address address;
        public SimpleOrderDto(Order order) {
            orderId = order.getId();
            name = order.getMember().getName();
            orderDate = order.getOrderDate();
            orderStatus = order.getStatus();
            address = order.getDelivery().getAddress();
        }
    }
    ```

    - 쿼리가 최악의 경우, 총 1 + N + N번 실행된다. (v1과 쿼리수 결과는 같다.)
      - `order` 조회 1번(`order` 조회 결과 수가 N이 된다.)
      - `order` -> `member` 지연 로딩 조회 N 번
      - `order` -> `delivery` 지연 로딩 조회 N 번



- 엔티티를 DTO로 변환 - 페치 조인 최적화

  - `OrderSimpleApiController` - 추가 코드

    ```java
    /**
     * V3. 엔티티를 조회해서 DTO로 변환(fetch join 사용O)
     * - fetch join으로 쿼리 1번 호출
     * 참고: fetch join에 대한 자세한 내용은 JPA 기본편 참고(정말 중요함)
     */
    @GetMapping("/api/v3/simple-orders")
    public List<SimpleOrderDto> ordersV3() {
        List<Order> orders = orderRepository.findAllWithMemberDelivery();
        List<SimpleOrderDto> result = orders.stream()
            .map(o -> new SimpleOrderDto(o))
            .collect(toList());
        return result;
    }
    ```

  - `OrderRepository` - 추가 코드

    ```java
    public List<Order> findAllWithMemberDelivery() {
        return em.createQuery(
            "select o from Order o" +
            " join fetch o.member m" +
            " join fetch o.delivery d", Order.class)
            .getResultList();
    }
    ```

    - 엔티티를 페치 조인(fetch join)을 사용해서 쿼리 1번에 조회



- JPA에서 DTO로 바로 조회

  - `OrderSimpleApiController` - 추가 코드

    ```JAVA
    private final OrderSimpleQueryRepository orderSimpleQueryRepository; //의존관계 주입
        /**
     * V4. JPA에서 DTO로 바로 조회
     * - 쿼리 1번 호출
     * - select 절에서 원하는 데이터만 선택해서 조회
     */
        @GetMapping("/api/v4/simple-orders")
        public List<OrderSimpleQueryDto> ordersV4() {
        return orderSimpleQueryRepository.findOrderDtos();
    }
    ```

  - `OrderSimpleQueryRepository` - 조회 전용 리포지토리

    ```JAVA
    @Repository
    @RequiredArgsConstructor
    public class OrderSimpleQueryRepository {
    
        private final EntityManager em;
    
        public List<OrderSimpleQueryDto> findOrderDtos() {
            return em.createQuery(
                    "select new jpabook.jpashop.repository.order.simplequery.OrderSimpleQueryDto(o.id, m.name, o.orderDate, o.status, d.address)" +
                            " from Order o" +
                            " join o.member m" +
                            " join o.delivery d", OrderSimpleQueryDto.class)
                    .getResultList();
        }
    }
    ```

    - `new` 명령어를 사용해서 JPQL의 결과를 DTO로 즉시 변환
    - SELECT 절에서 원하는 데이터를 직접 선택하므로 DB -> 애플리케이션 네트웍 용량 최적화(생각보다 미비)
    - 리포지토리 재사용성 떨어짐, API 스펙에 맞춘 코드가 리포지토리에 들어가는 단점
    - 리포지토리로 화면을 의존하고 있음



- 정리
  - 복잡한 쿼리용 리포지토리 패키지를 따로 둠
    - 엔티티 리포지토리는 가능한 순수한 엔티티를 조회
    - 유지보수성이 좋아짐
  - 엔티티를 DTO로 변환하거나, DTO로 바로 조회하는 두가지 방법은 각각 장단점이 있다
  - 쿼리 방식 선택 권장 순서
    1.  우선 엔티티를 DTO로 변환하는 방법을 선택한다.
    2. 필요하면 페치 조인으로 성능을 최적화 한다.
       - 대부분의 성능 이슈가 해결된다.
    3. 그래도 안되면 DTO로 직접 조회하는 방법을 사용한다.
    4. 최후의 방법은 JPA가 제공하는 네이티브 SQL이나 스프링 JDBC Template을 사용해서 SQL을 직접 사용한다

