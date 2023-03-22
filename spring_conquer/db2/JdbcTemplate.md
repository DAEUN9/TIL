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




- JdbcTemplate 적용1

  - 기본

    ```java
    @Slf4j
    @Repository
    public class JdbcTemplateItemRepositoryV1 implements ItemRepository {
        private final JdbcTemplate template;
        public JdbcTemplateItemRepositoryV1(DataSource dataSource) {
            this.template = new JdbcTemplate(dataSource);
        }
    ```

    - JdbcTemplateItemRepositoryV1 은 ItemRepository 인터페이스를 구현
    - this.template = new JdbcTemplate(dataSource)
      - JdbcTemplate은 dataSource가 필요 - 의존 관계 주입 받음
      - 생성자 내부에서 JdbcTemplate 생성
    - JdbcTemplate을 스프링 빈으로 직접 등록하게 주입받아도 됨

  - `save()`

    ```java
    @Override
    public Item save(Item item) {
        String sql = "insert into item (item_name, price, quantity) values (?, ?, ?)";
        KeyHolder keyHolder = new GeneratedKeyHolder();
    
        template.update(connection -> {
            //자동 증가 키
            PreparedStatement ps = connection.prepareStatement(sql, new String[]{"id"});
            ps.setString(1, item.getItemName());
            ps.setInt(2, item.getPrice());
            ps.setInt(3, item.getQuantity());
            return ps;
        }, keyHolder);
    
        long key = keyHolder.getKey().longValue();
        item.setId(key);
        return item;
    }
    ```

    - template.update() : 데이터를 변경할 때는 update() 를 사용
      - INSERT , UPDATE , DELETE SQL에 사용
      - 여기서 반환 값은 int, 영향 받은 로우 수 반환
    - PK 생성에 `identity`(auto increment) 방식을 상요하기 때문에 DB가 PK 대신 생성해줌
    - DB에 INSERT가 완료되어야 생성된 PK ID 값을 확인 가능
    - KeyHolder 와 connection.prepareStatement(sql, new String[]{"id"})
      - `id`를 지정해주어 INSERT 쿼리 실행 이후에 DB에서 생성된 ID 값 조회 가능
    - JdbcTemplate이 제공하는 `SimpleJdbcInsert` 기능으로훨씬 편리하게 사용 가능

  - `update()`

    ```java
    @Override
    public void update(Long itemId, ItemUpdateDto updateParam) {
        String sql = "update item set item_name=?, price=?, quantity=? where id=?";
        template.update(sql,
                updateParam.getItemName(),
                updateParam.getPrice(),
                updateParam.getQuantity(),
                itemId);
    }
    ```

    - template.update() : 데이터를 변경할 때는 update() 를 사용
      - ?에 바인딩할 파라미터를 순서대로 전달
      - 반환 값은 해당 쿼리의 영향을 받은 로우 수
        - 여기서는  where id=?를 지정해씩 때문에 영향받은 로우수는 최대 1개

  - findById()

    ```java
    @Override
    public Optional<Item> findById(Long id) {
        String sql = "select id, item_name, price, quantity from item where id = ?";
        try {
            Item item = template.queryForObject(sql, itemRowMapper(), id);
            return Optional.of(item);
        } catch (EmptyResultDataAccessException e) {
            return Optional.empty();
        }
    }
    ```

    - template.queryForObject()

      - 결과 로우가 하나일 때 사용
      - RowMapper 는 데이터베이스의 반환 결과인 ResultSet 을 객체로 변환한다.
      - 결과가 없으면 EmptyResultDataAccessException 예외가 발생한다.
      - 결과가 둘 이상이면 IncorrectResultSizeDataAccessException 예외가 발생한다.

    - ItemRepository.findById() 인터페이스는 결과가 없을 때 Optional 을 반환

      - 결과가 없으면 예외를 잡아서 Optional.empty 를 대신 반환하면 된다

    - queryForObjedt() 인터페이스 정의

      ```java
      <T> T queryForObject(String sql, RowMapper<T> rowMapper, Object... args) throws DataAccessException;
      ```

  - findAll()

    ```java
    @Override
    public List<Item> findAll(ItemSearchCond cond) {
        String itemName = cond.getItemName();
        Integer maxPrice = cond.getMaxPrice();
        String sql = "select id, item_name, price, quantity from item";
        //동적 쿼리
        if (StringUtils.hasText(itemName) || maxPrice != null) {
            sql += " where";
        }
        boolean andFlag = false;
        List<Object> param = new ArrayList<>();
        if (StringUtils.hasText(itemName)) {
            sql += " item_name like concat('%',?,'%')";
            param.add(itemName);
            andFlag = true;
        }
        if (maxPrice != null) {
            if (andFlag) {
                sql += " and";
            }
            sql += " price <= ?";
            param.add(maxPrice);
        }
        log.info("sql={}", sql);
        return template.query(sql, itemRowMapper(), param.toArray());
    }
    ```

    - template.query()

      - 결과가 하나 이상일 때 사용한다.
      - RowMapper 는 데이터베이스의 반환 결과인 ResultSet 을 객체로 변환한다
      - 결과가 없으면 빈 컬렉션을 반환한다

    - query() 인터페이스 정의

      ```java
      <T> List<T> query(String sql, RowMapper<T> rowMapper, Object... args) throws
      DataAccessException;
      ```

  - itemRowMapper()

    ```java
    private RowMapper<Item> itemRowMapper() {
        return (rs, rowNum) -> {
            Item item = new Item();
            item.setId(rs.getLong("id"));
            item.setItemName(rs.getString("item_name"));
            item.setPrice(rs.getInt("price"));
            item.setQuantity(rs.getInt("quantity"));
            return item;
        };
    }
    ```

    - DB 조회 결과를 객체로 변환할 때 사용
    - JdbcTemplate이 다음과 같은 루프를 돌려주고
    - 개발자는 RowMapper 를 구현해서 그 내부 코드만 채운다

    ```java
    while(resultSet 이 끝날 때 까지) {
    	rowMapper(rs, rowNum)
    }
    ```



- 동적 쿼리 문제

  - 결과를 검색하는 `findAll()`에서 어려운 부분은 사용자가 검색하는 값에 따라 실행하는 SQL이 동적으로 달라져야 한다는 점

  - 검색 조건이 없다면

    ```sql
    select id, item_name, price, quantity from item
    ```

  - 상품명으로 검색

    ```sql
    select id, item_name, price, quantity from item
    	where item_name like concat('%',?,'%')
    ```

  - 최대 가격으로 검색

    ```sql
    select id, item_name, price, quantity from item
    	where price <= ?
    ```

  - 상품명, 최대 가격 둘 다 검색

    ```sql
    select id, item_name, price, quantity from item
        where item_name like concat('%',?,'%')
         and price <= ?
    ```

  - 다양한 상황(ex) 순서)등도 모두 고려해야 함
  - MyBatis로 SQL을 직접 사용할 때 동적 쿼리를 쉽게 작성할 수 있다.



- 구성과 실행

  - JdbcTemplateV1Config

    ```java
    @Configuration
    @RequiredArgsConstructor
    public class JdbcTemplateV1Config {
    	private final DataSource dataSource;
        
        @Bean
        public ItemService itemService() {
        	return new ItemServiceV1(itemRepository());
        }
        
        @Bean
        public ItemRepository itemRepository() {
        	return new JdbcTemplateItemRepositoryV1(dataSource);
        }
    }
    ```

    - 메모리 저장소가 아니라 실제 DB에 연결하는 JdbcTemplate이 사용된다.

  - `ItemServiceApplication` - 변경

    ```java
    //@Import(MemoryConfig.class)
    @Import(JdbcTemplateV1Config.class)
    @SpringBootApplication(scanBasePackages = "hello.itemservice.web")
    public class ItemServiceApplication {}
    ```

  - `src/main/resources/application.properties`

    ```
    spring.profiles.active=local
    spring.datasource.url=jdbc:h2:tcp://localhost/~/test
    spring.datasource.username=sa
    ```

    - 스프링 부트가 해당 설정을 사용해서 커넥션 풀과 `DataSource`, 트랜잭션 매니저를 스프링빈으로 자동 등록

  - 로그 추가

    ```
    #jdbcTemplate sql log
    logging.level.org.springframework.jdbc=debug
    ```

    

- 이름 지정 파라미터1

  - JdbcTemplate은 기본적으로 파라미터를 순서대로 바인딩

  - SQL코드의 순서를 변경하면 파라미터가 가리키는 것이 달라지는 문제 발생

  - 모호함을 제거해서 코드를 명확하게 만드는 것이 유지보수 관점에서 매우 중요

  - 이름 지정 바인딩

    - `NamedParameterJdbcTemplate`으로 이름을 지정해서 파라미터를 바인딩하는 기능 제공

  - `save()`

    ```java
    @Override
    public Item save(Item item) {
        String sql = "insert into item (item_name, price, quantity) " +
        		"values (:itemName, :price, :quantity)";
        
        SqlParameterSource param = new BeanPropertySqlParameterSource(item);
        KeyHolder keyHolder = new GeneratedKeyHolder();
        template.update(sql, param, keyHolder);
        
        Long key = keyHolder.getKey().longValue();
        item.setId(key);
        return item;
    }
    ```

    - SQL에서 다음과 같이 `?` 대신에 `:파라미터이름` 을 받는 것을 확인할 수 있다
    - 추가로 NamedParameterJdbcTemplate 은 데이터베이스가 생성해주는 키를 매우 쉽게 조회하는 기능도 제공
    - `BeanPropertySqlParameterSource` 사용
      - 객체의 프로퍼티 이름을 SQL 파라미터 이름과 일치시킴

  - `update()`

    ```java
    @Override
    public void update(Long itemId, ItemUpdateDto updateParam) {
        String sql = "update item " +
            "set item_name=:itemName, price=:price, quantity=:quantity " +
            "where id=:id";
    
        SqlParameterSource param = new MapSqlParameterSource()
            .addValue("itemName", updateParam.getItemName())
            .addValue("price", updateParam.getPrice())
            .addValue("quantity", updateParam.getQuantity())
            .addValue("id", itemId); //이 부분이 별도로 필요하다.
        template.update(sql, param);
    }
    ```

    - `MapSqlParameterSource` 사용
      - Map 객체를 이용하여 SQL 문의 파라미터 값을 설정
      - `addValue()`는 Map에 파라미터를 추가하는 것과 비슷한 기능 사용



- 이름 지정 바인딩에서 자주 사용하는 파라미터 종류

  1. Map

     ```java
     Map<String, Object> param = Map.of("id", id);
     Item item = template.queryForObject(sql, param, itemRowMapper());
     ```

  2. MapSqlParameterSource

     ```java
     SqlParameterSource param = new MapSqlParameterSource()
         .addValue("itemName", updateParam.getItemName())
         .addValue("price", updateParam.getPrice())
         .addValue("quantity", updateParam.getQuantity())
         .addValue("id", itemId); //이 부분이 별도로 필요하다.
     template.update(sql, param);
     ```

  3. BeanPropertySqlParameterSource

     - 자바빈 프로퍼티 규약을 통해서 자동으로 파라미터 객체를 생성한다.

     - 예를 들어서 getItemName() , getPrice() 가 있으면 다음과 같은 데이터를 자동으로 만들어낸다.

       - key=itemName, value=상품명 값

       - key=price, value=가격 값

     ```java
     SqlParameterSource param = new BeanPropertySqlParameterSource(item);
     KeyHolder keyHolder = new GeneratedKeyHolder();
     template.update(sql, param, keyHolder);
     ```

     - 항상 사용할 수 있는 것은 아님
     - dto등에 원하는 정보가 없을 수 있다.



- BeanPropertyRowMapper 변화

  - JdbcTemplateItemRepositoryV1 - itemRowMapper()

    ```java
    private RowMapper<Item> itemRowMapper() {
        return (rs, rowNum) -> {
            Item item = new Item();
            item.setId(rs.getLong("id"));
            item.setItemName(rs.getString("item_name"));
            item.setPrice(rs.getInt("price"));
            item.setQuantity(rs.getInt("quantity"));
            return item;
        };
    }
    ```

  - JdbcTemplateItemRepositoryV2 - itemRowMapper()

    ```java
    private RowMapper<Item> itemRowMapper() {
         return BeanPropertyRowMapper.newInstance(Item.class); //camel 변환 지원
    }
    ```

    - BeanPropertyRowMapper 는 ResultSet 의 결과를 받아서 자바빈 규약에 맞추어 데이터를 변환한다

    - DB에서 조회한 결과가 `select id, price` 라면 다음과 같은 코드 작성해줌

      ```java
      Item item = new Item();
      item.setId(rs.getLong("id"));
      item.setPrice(rs.getInt("price"));
      ```

      - 실제로는 리플렉션 같은 기능 사용

  - 별칭

    - DB는 주로 언더스코어 표기법을 사용하기 때문에 컬럼 이름과 객체의 이름이 다를 수 있음
    - 별칭 사용
      - `select item_name as itemName`

    - BeanPropertyRowMapper는 언더스코어 표기법을 카멜으로 자동으로 변환해줌



- SimpleJdbcInsert

  ```java
  public JdbcTemplateItemRepositoryV3(DataSource dataSource) {
      this.template = new NamedParameterJdbcTemplate(dataSource);
      
      this.jdbcInsert = new SimpleJdbcInsert(dataSource)
              .withTableName("item")
              .usingGeneratedKeyColumns("id");
  //              .usingColumns("item_name", "price", "quantity"); //생략 가능
  }
  ```

  - `withTableName` : 데이터를 저장할 테이블 명을 지정

  - `usingGeneratedKeyColumns` : key 를 생성하는 PK 컬럼 명을 지정한다.

  - `usingColumns` : INSERT SQL에 사용할 컬럼을 지정한다. 특정 값만 저장하고 싶을 때 사용한다

    - 생략할 수 있다.

  - 생성 시점에 DB 테이블 메타 데이터 조회하기 때문에 usingColumns 생략 가능

  - `save()`

    ```java
    public Item save(Item item) {
        SqlParameterSource param = new BeanPropertySqlParameterSource(item);
        Number key = jdbcInsert.executeAndReturnKey(param);
        item.setId(key.longValue());
        return item;
    }
    ```

    - `jdbcInsert.executeAndReturnKey(param)` 을 사용해서 INSERT SQL을 실행하고, 생성된 키 값도 매우 편리하게 조회할 수 있다.



- JdbcTemplate 기능 정리
  - JdbcTemplate
    - 순서 기반 파라미터 바인딩을 지원한다.
  - NamedParameterJdbcTemplate
    - 이름 기반 파라미터 바인딩을 지원한다. (권장)
  - SimpleJdbcInsert
    - INSERT SQL을 편리하게 사용할 수 있다.
  - SimpleJdbcCall
    - 스토어드 프로시저를 편리하게 호출할 수 있다



- JdbcTemplate 사용법 정리

  - 단겆 조회 - 숫자 조회

    ```java
    int rowCount = jdbcTemplate.queryForObject("select count(*) from t_actor", Integer.class);
    ```

  - 단건 조회 - 숫자 조회, 파라미터 바인딩

    ```java
    int countOfActorsNamedJoe = jdbcTemplate.queryForObject(
     "select count(*) from t_actor where first_name = ?", Integer.class, "Joe");
    ```

  - 단건 조회 - 문자 조회

    ```java
    String lastName = jdbcTemplate.queryForObject(
        "select last_name from t_actor where id = ?",
        String.class, 1212L);
    ```

  - 단건 조회 - 객체 조회

    ```java
    Actor actor = jdbcTemplate.queryForObject(
        "select first_name, last_name from t_actor where id = ?",
        (resultSet, rowNum) -> {
            Actor newActor = new Actor();
            newActor.setFirstName(resultSet.getString("first_name"));
            newActor.setLastName(resultSet.getString("last_name"));
            return newActor;
        },
        1212L);
    ```

    - 결과를 객체로 매핑해야 하므로 RowMapper 를 사용해야 한다

  - 목록 조회 - 객체

    ```java
    private final RowMapper<Actor> actorRowMapper = (resultSet, rowNum) -> {
        Actor actor = new Actor();
        actor.setFirstName(resultSet.getString("first_name"));
        actor.setLastName(resultSet.getString("last_name"));
        return actor;
    };
    public List<Actor> findAllActors() {
         return this.jdbcTemplate.query("select first_name, last_name from t_actor",
    actorRowMapper);
    }
    
    ```

    - `RowMapper`를 분리했음

  - 등록

    ```java
    jdbcTemplate.update(
        "insert into t_actor (first_name, last_name) values (?, ?)",
        "Leonor", "Watling");
    ```

    - update는 int값을 반환 -> SQL 실행 결과에 영향을 받은 로우 수

  - 수정

    ```java
    jdbcTemplate.update(
        "update t_actor set last_name = ? where id = ?",
        "Banjo", 5276L);
    ```

  - 삭제

    ```java
    jdbcTemplate.update(
        "delete from t_actor where id = ?",
        Long.valueOf(actorId));
    ```

  - DDL

    - 임의의 SQL을 실행할 때는 `excute()`를 사용하면 됨

    ```java
    jdbcTemplate.execute("create table mytable (id integer, name varchar(100))");
    ```

  - 스토어드 프로시저 호출

    ```java
    dbcTemplate.update(
        "call SUPPORT.REFRESH_ACTORS_SUMMARY(?)",
        Long.valueOf(unionId));
    ```



- 정리
  - JdbcTemplate의 최대 단점은 동적 쿼리 문제를 해결하지 못한다는 점
  - SQL을 자바 코드로 작성하기 때문에 라인이 코드를 넘어갈 때마다 문자 더하기를 해주어야 함
  - 해결하기 위해 MyBatis 사용
