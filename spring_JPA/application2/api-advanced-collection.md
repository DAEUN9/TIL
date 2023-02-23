## API 개발 고급 - 컬렉션 조회 최적화

- 엔티티 직접 노출

  ```java
  /**
       * V1. 엔티티 직접 노출
       * - Hibernate5Module 모듈 등록, LAZY=null 처리
       * - 양방향 관계 문제 발생 -> @JsonIgnore
       */
  @GetMapping("/api/v1/orders")
  public List<Order> ordersV1() {
      List<Order> all = orderRepository.findAll();
      for (Order order : all) {
          order.getMember().getName(); //Lazy 강제 초기화
          order.getDelivery().getAddress(); //Lazy 강제 초기환
          List<OrderItem> orderItems = order.getOrderItems();
          orderItems.stream().forEach(o -> o.getItem().getName()); //Lazy 강제 초기화
      }
      return all;
  }
  ```

  - `orderItem` , `item` 관계를 직접 초기화하면 `Hibernate5Module` 설정에 의해 엔티티를 JSON으로 생성한다.
  - 양방향 연관관계면 무한 루프에 걸리지 않게 한곳에 `@JsonIgnore` 를 추가해야 한다
  - 엔티티를 직접 노출하므로 좋은 방법은 아니다.



- 엔티티를 DTO로 변환

  ```java
  @GetMapping("/api/v2/orders")
  public List<OrderDto> ordersV2() {
      List<Order> orders = orderRepository.findAll();
      List<OrderDto> result = orders.stream()
          .map(o -> new OrderDto(o))
          .collect(toList());
      return result;
  }
  ```

  - `OrderApiController` - 추가 코드

  ```java
  @Data
  static class OrderDto {
      private Long orderId;
      private String name;
      private LocalDateTime orderDate; //주문시간
      private OrderStatus orderStatus;
      private Address address;
      private List<OrderItemDto> orderItems;
      
      public OrderDto(Order order) {
          orderId = order.getId();
          name = order.getMember().getName();
          orderDate = order.getOrderDate();
          orderStatus = order.getStatus();
          address = order.getDelivery().getAddress();
          orderItems = order.getOrderItems().stream()
              .map(orderItem -> new OrderItemDto(orderItem))
              .collect(toList());
      }
  }
  
  @Data
  static class OrderItemDto {
      private String itemName;//상품 명
      private int orderPrice; //주문 가격
      private int count; //주문 수량
      public OrderItemDto(OrderItem orderItem) {
          itemName = orderItem.getItem().getName();
          orderPrice = orderItem.getOrderPrice();
          count = orderItem.getCount();
      }
  }
  ```

  - 지연 로딩으로 너무 많은 SQL 실행 SQL
  - 실행 수
    - `order` 1번
    - `member` , `address` N번(`order` 조회 수 만큼
    - `orderItem` N번(`order` 조회 수 만큼)
    - `item` N번(`orderItem` 조회 수 만큼)



- 엔티티를 DTO로 변환 - 페치 조인 최적화

  - `OrderApiController`에 추가

    ```java
    @GetMapping("/api/v3/orders")
    public List<OrderDto> ordersV3() {
        List<Order> orders = orderRepository.findAllWithItem();
        List<OrderDto> result = orders.stream()
            .map(o -> new OrderDto(o))
            .collect(toList());
        return result;
    }
    ```

  - `OrderRepository`에 추가

    ```java
    public List<Order> findAllWithItem() {
        return em.createQuery(
            "select distinct o from Order o" +
            " join fetch o.member m" +
            " join fetch o.delivery d" +
            " join fetch o.orderItems oi" +
            " join fetch oi.item i", Order.class)
            .getResultList();
    }
    ```

    - 페치 조인으로 SQL이 1번만 실행
    - `distinct` 를 사용한 이유는 1대다 조인이 있으므로 데이터베이스 row가 증가
      - 데이터 뻥튀기
      -  `order`가 컬렉션 페치 조인 때문에 중복 조회 되는 것을 막아준다
    - 단점
      - 페이징 불가능

  - **페치 조인을 사용하면 페이징이 불가능**

    - 페이징 예시 - 몇번째부터 몇개 가져오기
    - 하이버네이트는 경고 로그를 남기면서 모든 데이터를 DB에서 읽어오고, 메모리에서 페이징
    - 매우 위험

  - 컬렉션 페치 조인은 1개만 사용할 수 있다

    - 컬렉션 둘 이상에 페치 조인을 사용하면 안된다
    - 일대다의 다가 되어서 엄청 뻥튀기 됨
    - 데이터가 부정합하게 조회될 수 있다



- 엔티티를 DTO로 변환 - 페이징과 한계 돌파

  - 컬렉션을 페치 조인하면 페이징이 불가능하다.

    - 컬렉션을 페치 조인하면 일대다 조인이 발생하므로 데이터가 예측할 수 없이 증가한다.
    - 일다대에서 일(1)을 기준으로 페이징을 하는 것이 목적이다. 그런데 데이터는 다(N)를 기준으로 row 가 생성된다.
    - Order를 기준으로 페이징 하고 싶은데, 다(N)인 OrderItem을 조인하면 OrderItem이 기준이 되어버린다.

  - 한계 돌파

    - 먼저 ToOne(OneToOne, ManyToOne) 관계를 모두 페치조인
      - ToOne 관계는 row수를 증가시키지 않으므로 페이징 쿼리에 영향을 주지 않는다.
    - 컬렉션은 지연 로딩으로 조회한다
    - 지연 로딩 성능 최적화를 위해 `hibernate.default_batch_fetch_size` , `@BatchSize` 를 적용
      - `hibernate.default_batch_fetch_size`: 글로벌 설정
      - `@BatchSize`: 개별 최적화
      - 이 옵션을 사용하면 컬렉션이나, 프록시 객체를 한꺼번에 설정한 size 만큼 IN 쿼리로 조회한다

  - `OrderRepository`에 추가

    ```java
    public List<Order> findAllWithMemberDelivery(int offset, int limit) {
        return em.createQuery(
            "select o from Order o" +
            " join fetch o.member m" +
            " join fetch o.delivery d", Order.class)
            .setFirstResult(offset)
            .setMaxResults(limit)
            .getResultList();
    }
    ```

  - `OrderApiController`에 추가

    ```java
    /**
     * V3.1 엔티티를 조회해서 DTO로 변환 페이징 고려
     * - ToOne 관계만 우선 모두 페치 조인으로 최적화
     * - 컬렉션 관계는 hibernate.default_batch_fetch_size, @BatchSize로 최적화
     */
    @GetMapping("/api/v3.1/orders")
    public List<OrderDto> ordersV3_page(
        @RequestParam(value = "offset", defaultValue = "0") int offset,
        @RequestParam(value = "limit", defaultValue = "100") int limit) {
    
        List<Order> orders = orderRepository.findAllWithMemberDelivery(offset, limit);
    
        List<OrderDto> result = orders.stream()
            .map(o -> new OrderDto(o))
            .collect(toList());
        return result;
    }
    
    ```

    - `xToOne`관계만 페치 조인 했으므로 페이징 사용 가능

  - `application.yml` - 최적화 옵션

    ```yaml
    spring:
      jpa:
        properties:
    	  hibernate:
    		default_batch_fetch_size: 1000
    
    ```

    - 개별로 설정하려면 `@BatchSize` 를 적용하면 된다.
      - 컬렉션은 컬렉션 필드에, 엔티티는 엔티티 클래스에 적용

  - 장점
    - 쿼리 호출 수가 `1 + N` -> `1 + 1` 로 최적화 된다
    - 조인보다 DB 데이터 전송량이 최적화
      - 각각 조회하므로 전송해야할 중복 데이터가 없다
    - 페치 조인 방식과 비교해서 쿼리 호출 수가 약간 증가하지만, DB 데이터 전송량이 감소한다
    - 컬렉션 페치 조인은 페이징이 불가능 하지만 이 방법은 페이징이 가능
  - 결론
    - ToOne 관계는 페치 조인해도 페이징에 영향을 주지 않는다
    - ToOne 관계는 페치조인으로 쿼리 수를 줄이고 해결
    -  나머지는 `hibernate.default_batch_fetch_size` 로 최적화
  - `default_batch_fetch_size` 적당한 사이즈
    - 100~1000 사이를 선택하는 것을 권장
    - 총 메모리 사용량은 같음
    - 한번에 많이 
    - 순간 부하를 어디까지 견딜 수 있는지로 결정



- JPA에서 DTO 직접 조회

  - `OrderApiController`에 추가

    ```java
    private final OrderQueryRepository orderQueryRepository;
    @GetMapping("/api/v4/orders")
    public List<OrderQueryDto> ordersV4() {
        return orderQueryRepository.findOrderQueryDtos();
    }
    ```

  - `OrderQueryRepository`

    ```java
    @Repository
    @RequiredArgsConstructor
    public class OrderQueryRepository {
    
        private final EntityManager em;
    
        /**
         * 컬렉션은 별도로 조회
         * Query: 루트 1번, 컬렉션 N 번
         * 단건 조회에서 많이 사용하는 방식
         */
        public List<OrderQueryDto> findOrderQueryDtos() {
            //루트 조회(toOne 코드를 모두 한번에 조회)
            List<OrderQueryDto> result = findOrders();
    
            //루프를 돌면서 컬렉션 추가(추가 쿼리 실행)
            result.forEach(o -> {
                List<OrderItemQueryDto> orderItems = findOrderItems(o.getOrderId());
                o.setOrderItems(orderItems);
            });
            return result;
        }
    
        /**
         * 1:N 관계(컬렉션)를 제외한 나머지를 한번에 조회
         */
        private List<OrderQueryDto> findOrders() {
            return em.createQuery(
                    "select new jpabook.jpashop.repository.order.query.OrderQueryDto(o.id, m.name, o.orderDate, o.status, d.address)" +
                            " from Order o" +
                            " join o.member m" +
                            " join o.delivery d", OrderQueryDto.class)
                    .getResultList();
        }
    
        /**
         * 1:N 관계인 orderItems 조회
         */
        private List<OrderItemQueryDto> findOrderItems(Long orderId) {
            return em.createQuery(
                    "select new jpabook.jpashop.repository.order.query.OrderItemQueryDto(oi.order.id, i.name, oi.orderPrice, oi.count)" +
                            " from OrderItem oi" +
                            " join oi.item i" +
                            " where oi.order.id = : orderId", OrderItemQueryDto.class)
                    .setParameter("orderId", orderId)
                    .getResultList();
        }
    }
    ```

  - `OrderQueryDto`

    ```java
    @Data
    @EqualsAndHashCode(of = "orderId")
    public class OrderQueryDto {
        private Long orderId;
        private String name;
        private LocalDateTime orderDate; //주문시간
        private OrderStatus orderStatus;
        private Address address;
        private List<OrderItemQueryDto> orderItems;
        
        public OrderQueryDto(Long orderId, String name, LocalDateTime orderDate,
                             OrderStatus orderStatus, Address address) {
            this.orderId = orderId;
            this.name = name;
            this.orderDate = orderDate;
            this.orderStatus = orderStatus;
            this.address = address;
        }
    }
    ```

  - `OrderItemQueryDto`

    ```java
    @Data
    public class OrderItemQueryDto {
        @JsonIgnore
        private Long orderId; //주문번호
        private String itemName;//상품 명
        private int orderPrice; //주문 가격
        private int count; //주문 수량
        
        public OrderItemQueryDto(Long orderId, String itemName, int orderPrice,
                                 int count) {
            this.orderId = orderId;
            this.itemName = itemName;
            this.orderPrice = orderPrice;
            this.count = count;
        }
    }
    ```

    - `Query`: 루트 1번, 컬렉션 N 번 실행
    - ToOne(N:1, 1:1) 관계들을 먼저 조회하고, ToMany(1:N) 관계는 각각 별도로 처리한다. 
      - ToOne 관계는 조인해도 데이터 row 수가 증가하지 않는다.
      - ToMany(1:N) 관계는 조인하면 row 수가 증가한다.
    -  row 수가 증가하지 않는 ToOne 관계는 조인으로 최적화 하기 쉬우므로 한번에 조회하고
    - ToMany  관계는 최적화 하기 어려우므로 `findOrderItems()` 같은 별도의 메서드로 조회한다



- JPA에서 DTO 직접 조회 - 컬렉션 조회 최적화

  - `OrderApiController`에 추가

    ```java
    @GetMapping("/api/v5/orders")
    public List<OrderQueryDto> ordersV5() {
        return orderQueryRepository.findAllByDto_optimization();
    }
    ```

  - `OrderQueryRepository`에 추가

    ```java
    /**
     * 최적화
     * Query: 루트 1번, 컬렉션 1번
     * 데이터를 한꺼번에 처리할 때 많이 사용하는 방식
     *
     */
    public List<OrderQueryDto> findAllByDto_optimization() {
        //루트 조회(toOne 코드를 모두 한번에 조회)
        List<OrderQueryDto> result = findOrders();
    
        //orderItem 컬렉션을 MAP 한방에 조회
        Map<Long, List<OrderItemQueryDto>> orderItemMap =
            findOrderItemMap(toOrderIds(result));
    
        //루프를 돌면서 컬렉션 추가(추가 쿼리 실행X)
        result.forEach(o -> o.setOrderItems(orderItemMap.get(o.getOrderId())));
    
        return result;
    }
    
    private List<Long> toOrderIds(List<OrderQueryDto> result) {
        return result.stream()
            .map(o -> o.getOrderId())
            .collect(Collectors.toList());
    }
    
    private Map<Long, List<OrderItemQueryDto>> findOrderItemMap(List<Long> orderIds) {
        
        List<OrderItemQueryDto> orderItems = em.createQuery(
            "select new jpabook.jpashop.repository.order.query.OrderItemQueryDto(oi.order.id, i.name, oi.orderPrice, oi.count)" +
            " from OrderItem oi" +
            " join oi.item i" +
            " where oi.order.id in :orderIds", OrderItemQueryDto.class)
            .setParameter("orderIds", orderIds)
            .getResultList();
    
        return orderItems.stream()
            .collect(Collectors.groupingBy(OrderItemQueryDto::getOrderId));
        
        // Map<Long, List<OrderItemQueryDto> orderItemMap = orderItems.stream()
        // .collect(Collectors.groupingBy(orderItemQueryDto -> orderItemQueryDto.getOrderId()));
        // result.forEach(o -> o.setOrdrItems(orderItemMap.get(o.getOrderId())));
    }
    
    ```

    - `Query`: 루트 1번, 컬렉션 1번
    - ToOne 관계들을 먼저 조회하고, 여기서 얻은 식별자 `orderId`로 ToMany 관계인 `OrderItem` 을 한꺼번에 조회
    - MAP을 사용해서 매칭 성능 향상(O(1))



- JPA에서 DTO로 직접 조회, 플랫 데이터 최적화

  - `OrderApiController`에 추가

    ```java
    @GetMapping("/api/v6/orders")
    public List<OrderQueryDto> ordersV6() {
        List<OrderFlatDto> flats = orderQueryRepository.findAllByDto_flat();
    
        return flats.stream()
            .collect(groupingBy(o -> new OrderQueryDto(o.getOrderId(), o.getName(), o.getOrderDate(), o.getOrderStatus(), o.getAddress()),
                                mapping(o -> new OrderItemQueryDto(o.getOrderId(), o.getItemName(), o.getOrderPrice(), o.getCount()), toList())
                               )).entrySet().stream()
            .map(e -> new OrderQueryDto(e.getKey().getOrderId(), e.getKey().getName(), e.getKey().getOrderDate(), e.getKey().getOrderStatus(), e.getKey().getAddress(), e.getValue()))
            .collect(toList());
    }
    ```

  - `OrderQueryDto`에 생성자 추가

    ```java
    public OrderQueryDto(Long orderId, String name, LocalDateTime orderDate,
                         OrderStatus orderStatus, Address address, List<OrderItemQueryDto> orderItems) {
        this.orderId = orderId;
        this.name = name;
        this.orderDate = orderDate;
        this.orderStatus = orderStatus;
        this.address = address;
        this.orderItems = orderItems;
    }
    ```

  - `OrderQuertyRepository`에 추가

    ```java
    public List<OrderFlatDto> findAllByDto_flat() {
        return em.createQuery(
            "select new jpabook.jpashop.repository.order.query.OrderFlatDto(o.id, m.name, o.orderDate, o.status, d.address, i.name, oi.orderPrice, oi.count)" +
            " from Order o" +
            " join o.member m" +
            " join o.delivery d" +
            " join o.orderItems oi" +
            " join oi.item i", OrderFlatDto.class)
            .getResultList();
    }
    ```

  - `OrderFlatDto`

    ```java
    @Data
    public class OrderFlatDto {
    
        private Long orderId;
        private String name;
        private LocalDateTime orderDate; //주문시간
        private Address address;
        private OrderStatus orderStatus;
    
        private String itemName;//상품 명
        private int orderPrice; //주문 가격
        private int count;      //주문 수량
    
        public OrderFlatDto(Long orderId, String name, LocalDateTime orderDate, OrderStatus orderStatus, Address address, String itemName, int orderPrice, int count) {
            this.orderId = orderId;
            this.name = name;
            this.orderDate = orderDate;
            this.orderStatus = orderStatus;
            this.address = address;
            this.itemName = itemName;
            this.orderPrice = orderPrice;
            this.count = count;
        }
    
    }
    ```

    - Query: 1번
    - 단점
      - 쿼리는 한번이지만 조인으로 인해 DB에서 애플리케이션에 전달하는 데이터에 중복 데이터가 추가
      - 상황에 따라 V5 보다 더 느릴 수 도 있다.
      - 애플리케이션에서 추가 작업이 크다.
      - 페이징 불가능



- 정리
  - 엔티티 조회
    - 엔티티를 조회해서 그대로 반환 : V1
    - 엔티티 조회 후 DTO로 변환: V2
    - 페치 조인으로 쿼리 수 최적화: V3
    - 컬렉션 페이징과 한계 돌파: V3.1
      - 컬렉션은 페치 조인시 페이징이 불가능
      - ToOne 관계는 페치 조인으로 쿼리 수 최적화
      - 컬렉션은 페치 조인 대신에 지연 로딩을 유지하고 배치 사이즈로 최적화
  - DTO 직접 조회
    - JPA에서 DTO를 직접 조회: V4
    - 컬렉션 조회 최적화
      - 일대다 관계인 컬렉션은 IN 절을 활용해서 메모리에 미리 조회해서 최적화 : V5
    - 플랫 데이터 최적화
      - JOIN 결과를 그대로 조회 후 애플리케이션에서 원하는 모양으로 직접 변환 : V6
  - 권장 순서
    1. 엔티티 조회 방식으로 우선 접근
       1. 페치조인으로 쿼리 수를 최적화
       2. 컬렉션 최적화
          1. 페이징 필요 `hibernate.default_batch_fetch_size` , `@BatchSize` 로 최적화
          2. 페이징 필요X -> 페치 조인 사용
    2. 엔티티 조회 방식으로 해결이 안되면 DTO 조회 방식 사용
    3. DTO 조회 방식으로 해결이 안되면 NativeSQL or 스프링 JdbcTemplat
  - 참고
    - 엔티티 조회 방식은 페치 조인이나 배치 사이즈 같이 코드를 거의 수정하지 않고 옵션만 약간 변경해서 다양한 성능 최적화 시도 가능
    - 반면 dto 직접 조회하는 형식은 성능 최적화에 많은 코드 변경이 필요하다
    - dto 직접 조회는 쓰지 말자 엔티티 조회 방식으로 부족한 경우는 캐시 사용 등으로 최적화가 필요하다.
    - 엔티티 조회 방식은 JPA가 많은 부분을 최적화 해주기 때문에, 단순한 코드를 유지하면서, 성능을 최적화 할 수 있다
    - DTO 조회 방식은 SQL을 직접 다루는 것과 유사하기 때문에 성능과 코드 복잡도 사이에 줄타기를 해야 한다.
  - DTO 조회 방식의 선택지
    - 쿼리가 1번 실행된다고 V6가 항상 좋은 방법은 아님
    - V4: 특정 주문 한건만 조회하면 이 방식도 성능이 잘 나옴
    - V5: 여러 주문을 한꺼번에 조회
    - V6: 페이징 불가, 데이터가 많으면 중복 전송이 증가해서 V5와 성능 차이 미비