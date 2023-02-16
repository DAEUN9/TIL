## 메시지, 국제화

- 메시지

  - 다양한 메시지를 한 곳에서 관리하도록 하는 기능

  - `messages.properties`

    ```
    item=상품
    item.id=상품 ID
    item.itemName=상품명
    item.price=가격
    item.quantity=수량
    ```

  - 각 HTML들은 해당 데이터를 key 값으로 불러서 사용
  - `addForm.html`
    - `<label for="itemName" th:text="#{item.itemName}"></label>`
  - `editForm.html`
    - `<label for="itemName" th:text="#{item.itemName}"></label>`

- 국제화

  - 메시지 설정 파일을 각 나라별로 별도로 관리하면 서비스를 국제화 할 수 있다.

  - `messages_en.properties`

    ```
    item=Item
    item.id=Item ID
    item.itemName=Item Name
    item.price=price
    item.quantity=quantity
    ```

  - `messages_ko.properties`

    ```
    item=상품
    item.id=상품 ID
    item.itemName=상품명
    item.price=가격
    item.quantity=수량
    ```

  - 언어 선택 방법
    - HTTP `accept-language` 헤더 값 사용
    - 사용자가 직접 언어 선택, 쿠키 사용



- 스프링 메시지 소스 설정

  - 메시지 관리 기능을 사용하려면 인터페이스인 `MessageSource`를 스프링 빈으로 등록

  - 즉, 구현체인 `ResourceBundleMessageSource`를 스프링 빈으로 등록

  - 스프링 부트 메시지 소스 설정

    - `application.properties`

      ```
      spring.messages.basename=messages,config.i18n.messages
      ```

  - 스프링 부트 메시지 소스 기본 값

    - `spring.messages.basename=messages`
    - 별도 설정을 하지 않으면 `messages`라는 이름으로 기본 등록
    - `messages_en.properties` , `messages_ko.properties` , `messages.properties` 파일만 등록하면 자동으로 인식

  - 메시지 파일 만들기

    - 주의! 파일명은 `message`가 아니라 `messages`

    - `/resources/messages.properties`

      ```
      hello=안녕
      hello.name=안녕 {0}
      ```

    - `/resources/messages_en.properties`

      ```
      hello=hello
      hello.name=hello {0}
      ```



- 스프링 메시지 소스 사용

  - ```java
    @Autowired
    MessageSource ms;
    @Test
    void helloMessage() {
        String result = ms.getMessage("hello", null, null);
        assertThat(result).isEqualTo("안녕");
    }
    ```

    - `code` : "hello"
    - `args`: null
    - `locale`: null
    - `locale` 정보가 없으면 `besecame`에서 설정한 기본 이름 메시지 파일 조회
    - `messages.properties`파일에서 데이터 조회

  - ```java
    @Test
    void notFoundMessageCode() {
        assertThatThrownBy(() -> ms.getMessage("no_code", null, null))
            .isInstanceOf(NoSuchMessageException.class);
    }
    @Test
    void notFoundMessageCodeDefaultMessage() {
        String result = ms.getMessage("no_code", null, "기본 메시지", null);
        assertThat(result).isEqualTo("기본 메시지");
    }
    ```

    - 메시지가 없는 경우에는 `NoSuchMessageException` 발생
    - 메시지가 없어도 기본 메시지(`defaultMessage`)를 사용하면 기본 메시지 반환

  - ```java
    @Test
    void argumentMessage() {
        String result = ms.getMessage("hello.name", new Object[]{"Spring"}, null);
        assertThat(result).isEqualTo("안녕 Spring");
    }
    ```

    - 메시지의 `{0}` 는 매개변수를 전달해서 치환 가능
    - `hello.name=안녕 {0}` -> Spring 단어를 매개변수로 전달 -> `안녕 Spring`

  - 국제화 파일 선택

    - locale 정보 기반으로 탐색
    - `en_US`의 경우 `messages_en_US` -> `messages_en` -> `messages` 순서로 찾는다



- 타임리프 메시지 적용
  - 메시지 표현식 `#{...}` 를 사용하면 스프링의 메시지를 편리하게 조회 가능
  - 렌더링 전
    - `<th th:text="#{label.item}"></th>`
  - 렌더링 후
    - `<th>상품</th>`
  - 파라미터 사용법
    - `hello.name=안녕 {0}`
    - `<p th:text="#{hello.name(${item.itemName})}"></p>`



- 웹 애플리케이션에 국제화 적용하기

  - `LocaleResolver`

    - 스프링은 `Locale` 선택 방식을 변경할 수 있도록 `LocaleResolver` 라는 인터페이스를 제공

    - 스프링 부트는 기본으로 `Accept-Language` 를 활용하는 `AcceptHeaderLocaleResolver` 를 사용

    - ```java
      public interface LocaleResolver {
          
          Locale resolveLocale(HttpServletRequest request);
          
          void setLocale(HttpServletRequest request,
                         @Nullable HttpServletResponse response,
                         @Nullable Locale locale);
      }
      ```

  - `LocaleResolver` 변경

    - `LocaleResolver`를 변경하거나
    - 쿠키나 세션 기반의 `Locale` 선택 기능을 사용 가능