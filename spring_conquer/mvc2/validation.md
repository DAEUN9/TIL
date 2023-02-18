## 검증

- 클라이언트 검증, 서버 검증
  - 클라이언트 검증은 조작할 수 있으므로 보안에 취약하다
  - 서버만으로 검증하면, 즉각적인 고객 사용성이 부족해진다
  - 둘을 적절히 섞어서 사용하되, 최종적으로 서버 검증은 필수
  - API 방식을 사용하면 API 스펙을 잘 정의해서 검증 오류를 API 응답 결과에 잘 남겨주어야 함



- 검증 직접 처리
  - 상품 등록 폼에서 검증이 실패하면 어떤 값을 잘못 입력했는지 친절히 알려주어야 함
  - 검증 오류가 발생하면 입력 폼을 다시 보여줌
  - 검증 오류가 발생해도 고객이 입력한 데이터가 유지
- 남은 문제점
  - 뷰 템플릿 중복 처리
  - 타입 오류 처리가 필요
  - 문자는 바인딩이 불가능하므로 고객이 입력한 문자 사라짐
  - 결국 고객이 입력한 값도 어디엔가 별도로 관리 필요



- BindingResult1

  - `BindingResult bindingResult` 파라미터의 위치는 `@ModelAttribute Item item` 다음에 와야 한다

  - 자동으로 뷰에 같이 넘어감

  - 특정 필드를 넘어서는 오류가 있으면 `ObjectError` 객체를 생성해서 `bindingResult`에 담기

  - `FieldError`

    - `public FieldError(String objectName, String field, String defaultMessage) {}`
    - `objectName` : `@ModelAttribute` 이름
    - `field` : 오류가 발생한 필드 이름
    - `defaultMessage` : 오류 기본 메시지

  - 타임리프 스프링 검증 오류 통합 기능

    > 타임리프는 스프링의 BindingResult 를 활용해서 편리하게 검증 오류를 표현하는 기능을 제공

    - `#fields` : `#fields` 로 `BindingResult` 가 제공하는 검증 오류에 접근할 수 있다.
    - `th:errors` : 해당 필드에 오류가 있는 경우에 태그를 출력한다. `th:if` 의 편의 버전이다. 
    - `th:errorclass` : `th:field` 에서 지정한 필드에 오류가 있으면 class 정보를 추가한다.

  - ```html
    <div>
        <label for="price" th:text="#{label.item.price}">가격</label>
        <input type="text" id="price" th:field="*{price}"
               th:errorclass="field-error" class="form-control"
               placeholder="가격을 입력하세요">
        <div class="field-error" th:errors="*{price}">
            가격 오류
        </div>
    </div>
    ```



- BindingResult2
  - `BindingResult`가 있으면
    - `@ModelAttribute`에 데이터 바인딩 시 오류가 발생해도 컨트롤러가 호출
  - `BindingResult`가 없으면
    - 400 오류가 발생하면서 컨트롤러 호출 X
    - 오류 페이지로 이동
  - `BindingResult`에 검증 오류를 적용하는 3가지 방법
    - 스프링이 `FieldError` 생성해서 `BindingResult`에 넣어줌
    - 개발자가 직접 넣어줌
    - `Validator` 사용
  - `BidingResult`는 `Errors`를 상속 받음
    - `Errors`보다 `BidingResult`에서 추가적인 기능 제공
  - `BindingResult`는 검증할 대상  바로 다음에 와야 함
  - `BindingResult`는 `Model`에 자동으로 포함



- FieldError

  - 생성자

    ```java
    public FieldError(String objectName, String field, String defaultMessage);
    public FieldError(String objectName, String field, @Nullable Object 
                      rejectedValue, boolean bindingFailure, @Nullable String[] codes,
                      @Nullable Object[] arguments, @Nullable String defaultMessage)
    ```

  - 파라미터 목록

    - `objectName` : 오류가 발생한 객체 이름
    - `field` : 오류 필드
    - `rejectedValue` : 사용자가 입력한 값(거절된 값) 
    - `bindingFailure` : 타입 오류 같은 바인딩 실패인지, 검증 실패인지 구분 값
    - `codes `: 메시지 코드
    - `arguments` : 메시지에서 사용하는 인자 
    - `defaultMessage` : 기본 오류 메시지

  - 오류 발생시 사용자 입력 값 유지

    ```java
    new FieldError("item", "price", item.getPrice(), false, null, null,
                   "가격은 1,000 ~ 1,000,000 까지 허용합니다.")
    ```

    - `rejectedValue`에 오류 발생시 사용자 입력 값을 저장

  - 타임리프의 사용자 입력 값 유지

    - `th:field="*{price}"`
    - 정상 상황에서는 모델의 객체의 값을 사용(`model.getPrice`)
    - 오류가 발생하면 `FieldError`에서 `field`가 `price`인 에러를 꺼내서 출력

- ObjectError - 글로벌 오류

  ```java
  public ObjectError(String objectName, String defaultMessage) {}
  ```

  

- 오류 코드와 메시지 처리1

  - `FieldError` , `ObjectError` 의 생성자는 `codes` , `arguments` 를 제공한다

    - 오류 발생시 오류 코드로 메시지를 찾기 위해 사용
    - `codes` : 메시지 코드
    - `arguments` : 메시지에서 사용하는 인자

  - errors 메시지 파일 생성

    - ```
      // src/main/resources/errors.properties
      
      required.item.itemName=상품 이름은 필수입니다.
      range.item.price=가격은 {0} ~ {1} 까지 허용합니다.
      max.item.quantity=수량은 최대 {0} 까지 허용합니다.
      totalPriceMin=가격 * 수량의 합은 {0}원 이상이어야 합니다. 현재 값 = {1}
      ```

    - ```
      // application.properties
      
      spring.messages.basename=messages,errors
      ```

      - `errors_en.properties` 등 오류 메시지도 국제화 처리 가능

    - ```java
      // 컨트롤러에서 필드 에러 생성 부분
      
      //range.item.price=가격은 {0} ~ {1} 까지 허용합니다.
      new FieldError("item", "price", item.getPrice(), false, new String[]
      {"range.item.price"}, new Object[]{1000, 1000000}
      ```

      ```java
      public FieldError(String objectName, String field, @Nullable Object 
                        rejectedValue, boolean bindingFailure, @Nullable String[] codes,
                        @Nullable Object[] arguments)
      ```

    - 메시지 코드는 하나가 아니라 배열로 여러 개 전달 가능
      - 순서대로 매칭해서 처음 매칭되는 메시지 사용

  - 실행해보면 `MessageSource`를 찾아서 메시지 조회

    - `locale` 지원



- 오류 코드와 메시지 처리2

  - `FieldError` , `ObjectError` 는 다루기 너무 번거롭다

  - `BindingResult` 는 이미 본인이 검증해야 할 객체인 `target` 을 알고 있다

    - 검증해야 할 객체 바로 뒤에 오기 때문

  - `rejectValue()` , `reject() `를 사용해서 기존 코드를 단순화

    - `FieldError` , `ObjectError` 를 직접 생성하지 않고, 깔끔하게 검증 오류를 다룰 수 있다

    - `rejectValue()`

      ```java
      void rejectValue(@Nullable String field, String errorCode,
      @Nullable Object[] errorArgs, @Nullable String defaultMessage);
      ```

      - `field` : 오류 필드명
      - `errorCode` : 오류 코드
        - 메시지에 등록된 코드가 아니다.
        - `messageResolver`를 위한 오류 코드
      - `errorArgs` : 오류 메시지에서 {0} 을 치환하기 위한 값
      - `defaultMessage` : 오류 메시지를 찾을 수 없을 때 사용하는 기본 메시지

      ```JAVA
      bindingResult.rejectValue("price", "range", new Object[]{1000, 1000000}, null
      ```

      - `errors.properties`에 있는 코드를 직접 입력하지 않았는데 메시지 정상 출력

  - 축약된 오류 코드

    - `range.item.price` -> `range`
    - 규칙이 있는 것처럼 보임
    - `MessageCodesResolver`를 이해해야 함



- 오류 코드와 메시지 처리3

  - 오류 코드를 단순하게 만들면 범용성이 좋지만 세밀하게 작성하기 어려움

  - 가장 좋은 방법은 범용성으로 사용하다가, 세밀한 내용이 적용되도록 메시지에 단계를 두는 방법

    ```
    #Level1
    required.item.itemName: 상품 이름은 필수 입니다.
    #Level2
    required: 필수 값 입니다.
    ```

  - 디테일한 메시지를 우선 조회하고, 없으면 좀 더 범용적인 메시지 선택
  - `MessageCodesResolver`로 이러한 기능 지원



- 오류 코드와 메시지 처리4

  - `MessageCodesResolverTest`

    ```java
    MessageCodesResolver codesResolver = new DefaultMessageCodesResolver();
    
    @Test
    void messageCodesResolverObject() {
        String[] messageCodes = codesResolver.resolveMessageCodes("required","item");
        assertThat(messageCodes).containsExactly("required.item", "required");
    }
    ```

    - `bindingResult`의 `rejectValue`가 내부적으로 `codesResolver` 호출
      - `ObjectError`, `FieldError` 생성
    - `MessageCodesResolver` 인터페이스이고 `DefaultMessageCodesResolver` 는 기본 구현체

  - `DefaultMessageCodesResolver`의 기본 메시지 생성 규칙

    - 객체 오류

      ```
      객체 오류의 경우 다음 순서로 2가지 생성
      1.: code + "." + object name
      2.: code
      
      예) 오류 코드: required, object name: item
      1.: required.item
      2.: required
      ```

    - 필드 오류

      ```
      필드 오류의 경우 다음 순서로 4가지 메시지 코드 생성
      1.: code + "." + object name + "." + field
      2.: code + "." + field
      3.: code + "." + field type
      4.: code
      
      예) 오류 코드: typeMismatch, object name "user", field "age", field type: int
      1. "typeMismatch.user.age"
      2. "typeMismatch.age"
      3. "typeMismatch.int"
      4. "typeMismatch"
      ```

  - 동작 방식

    - `rejectValue()` , `reject()` 는 내부에서 `MessageCodesResolver` 를 사용한다. 여기에서 메시지 코드들을 생성한다.
    - `FieldError` , `ObjectError` 의 생성자를 보면, 오류 코드를 하나가 아니라 여러 오류 코드를 가질 수 있다.
    - `MessageCodesResolver` 를 통해서 생성된 순서대로 오류 코드를 보관한다
    - 이 부분을 `BindingResult` 의 로그를 통해서 확인해보자.
      - `codes [range.item.price, range.price, range.java.lang.Integer, range]`

  - 오류 메시지 출력

    - 타임리프 화면을 렌더링 할 때 `th:errors` 실행
      - 오류가 있다면 생성된 오류 메시지 코드를 순서대로 돌아가면서 메시지를 찾는다
      - 없으면 디폴트 메시지를 출력한다



- 오류 코드와 메시지 처리5
  - 오류 코드 관리 전략
    - 구체적인 것을 먼저 만들어 주고, 덜 구체적인 것을 가장 나중에 만듦
    - 크게 중요하지 않은 메시지는 범용성이 있는 메시지로 끝내고
    - 중요한 메시지는 꼭 필요할 때 구체적으로 적어서 사용하자
  - `itemName` 의 경우 `required` 검증 오류 메시지가 발생하면 다음 코드 순서대로 메시지가 생성
    1. `required.item.itemName`
    2. `required.itemName`
    3. `required.java.lang.String`
    4. `required`
  - 생성된 메시지 코드를 기반으로 순서대로 `MessageSource`에서 메시지를 찾음
  - 크게 중요하지 않은 오류 메시지는 기존에 정의된 것을 그냥 재활용!



- `ValidationUtils`

  - 사용 전

    ```java
    if (!StringUtils.hasText(item.getItemName())) {
        bindingResult.rejectValue("itemName", "required", "기본: 상품 이름은 필수입니다.");
    }
    ```

  - 사용 후

    ```java
    ValidationUtils.rejectIfEmptyOrWhitespace(bindingResult, "itemName",
    "required");
    ```

    - 다음과 같이 한 줄로 가능, 제공하는 기능은 `Empty`, 공백 같은 단순한 기능만 제공



- 오류 코드와 메시지 처리6
  - 검증 오류 코드는 2가지로 나눌 수 있음
    - 개발자가 직접 설정한 오류 코드 -> `rejectValue()` 직접 호출
    - 스프링이 직접 검증 오류에 추가한 경우(주로 타입 오류)
  - `typeMismatch`
    - 타입 오류가 발생하면 스프링이 사용
    - 숫자 필드(`item.price`)에 문자를 입력하면 자동으로 메시지 코드 생성
      - `typeMismatch.item.price`
      - `typeMismatch.price`
      - `typeMismatch.java.lang.Integer`
      - `typeMismatch`



- Validator 분리1

  - 컨트롤러에 검증 로직이 많으므로 역할을 분리하자

  - 스프링은 검증을 체계적으로 제공하기 위해 `Validator` 인터페이스 제공

    ```java
    public interface Validator {
        boolean supports(Class<?> clazz);
        void validate(Object target, Errors errors);
    }
    ```

    - `supports() {}`: 해당 검증기를 지원하는 여부 확인
    - `validate(Object target, Errors errors)` : 검증 대상 객체와 `BindingResult`



- Validator 분리2

  - `WebDataBinder`

    - 스프링 파라미터 바인딩 역할
    - 내부에 검증 기능 포함
    - 별로 안중요

    ```java
    @InitBinder
    public void init(WebDataBinder dataBinder) {
        log.info("init binder {}", dataBinder);
        dataBinder.addValidators(itemValidator);
    }
    ```

    - 컨트롤러 호출시 실행
    - 해당 컨트롤러에 검증기 자동 적용

  - `@Validated`

    - 검증 대상 앞에 붙임

    - 검증기를 실행하라는 애노테이션

      - `WebDataBinder`에 등록한 검증기를 찾아서 실행

    - 검증기 구분은 `supports()` 사용

      - 여러 개 검증기가 등록되면 구분이 필요

      ```java
      @Component
      public class ItemValidator implements Validator {
          
          @Override
          public boolean supports(Class<?> clazz) {
              return Item.class.isAssignableFrom(clazz);
          }
          
          @Override
          public void validate(Object target, Errors errors) {...}
      }
      ```

      - 여기서는 `supports(Item.class)` 호출되고 결과가 `true` 이면 `ItemValidator`의 `validate()` 적용

  - 글로벌 설정으로 `validator` 적용 가능

    ```java
    @SpringBootApplication
    public class ItemServiceApplication implements WebMvcConfigurer {
        public static void main(String[] args) {
            SpringApplication.run(ItemServiceApplication.class, args);
        }
        
        @Override
        public Validator getValidator() {
            return new ItemValidator();
        }
    }
    ```

  - `@Validated`, `@Valid`
    - `@Valid`는 자바 표준 검증 애노테이션
      - 의존 관계 추가 필요
      - `implementation 'org.springframework.boot:spring-boot-starter-validation'`
    - `@Validated`는 스프링 전용 검증 애노테이션