## Bean Validation

- Bean Validation
  - 특정한 구현체가 아니라 기술 표준
  - 검증 애노테이션과 여러 인터페이스의 모음
  - 하이버네이트 `Validator`
    - Bean Validation을 구현한 기술중에 일반적으로 사용하는 구현체
    - 이름이 하이버네이트가 붙었지만 `ORM`과는 관련없음
  - Jakarta Bean Validation
    - `jakarta.validation-api` : Bean Validation 인터페이스
    - `hibernate-validator` : 구현체



- 검증 애노테이션
  - `@NotBlank` : 빈값 + 공백만 있는 경우를 허용하지 않는다.
  - `@NotNull` : null 을 허용하지 않는다.
  - `@Range(min = 1000, max = 1000000)` : 범위 안의 값이어야 한다.
  - `@Max(9999)` : 최대 9999까지만 허용한다.



- 스프링 적용
  - 스프링 부트는 자동으로 글로벌 Validator로 등록
    - `LocalValidatorFactoryBean` 을 글로벌 `Validator`로 등록
    -  `@Valid` , `@Validated` 만 적용하면 된다.
    - 검증 오류가 발생하면, `FieldError` , `ObjectError` 를 생성해서 `BindingResult` 에 담아준다
  - 주의
    - 직접 글로벌 Validator를 등록하면,  Bean Validator를 글로벌 `Validator`로 등록하지 않음



- 검증 순서
  1. `@ModelAttribute` 각각의 필드에 타입 변환 시도
     1. 성공하면 다음으로
     2. 2. 실패하면 `typeMismatch` 로 `FieldError` 추가
  2.  `Validator` 적용
     - 바인딩이 성공한 필드만 Bean Validation 적용



- 에러 코드

  - `Validator` 애노테이션 이름으로 오류 코드 등록

  - `MessageCodesResolver`를 통해 다양한 메시지 코드가 순서대로 생성

    ```
    @NotBlank
    NotBlank.item.itemName
    NotBlank.itemName
    NotBlank.java.lang.String
    NotBlank
    ```

  - BeanValidation 메시지 찾는 순서
    1. 생성된 메시지 코드 순서대로 `messageSource` 에서 메시지 찾기
    2. 애노테이션의 `message` 속성 사용 -> `@NotBlank(message = "공백! {0}")`
    3. 라이브러리가 제공하는 기본 값 사용 -> 공백일 수 없습니다.



- 오브젝트 오류

  - `@ScriptAssert()`

    ```java
    @Data
    @ScriptAssert(lang = "javascript",
                  script = "_this.price * _this.quantity >= 10000")
                  public class Item {
                      //...
                  }
    ```

    - 제약 조건이 너무 많고 복잡

  - 오브젝트 오류 관련 부분만 직접 자바 코드로 작성하는 것 권장



- Bean Validation - 한계
  - 만약 수정할 때 `id` 값이 필수이므로 엔티티에 `@NotNull`을 적용한다면
    - 등록에서 문제 발생
    - 등록시에는 `id`가 없기 때문
  - 검증 조건의 충돌이 발생할 수 있다



- 동일한 모델 객체를 등록할 때, 수정할 때 다르게 검증하는 법
  - BeanValidation의 `groups `기능을 사용한다.
  - Item을 직접 사용하지 않고, `ItemSaveForm`, `ItemUpdateForm` 같은 폼 전송을 위한 별도의 모델 객체를 만들어서 사용한다



- gropus

  - 등록시 검증할 기능과 수정시에 검증할 기능을 각각 그룹으로 나누어 적용

  ```java
  @Data
  public class Item {
      @NotNull(groups = UpdateCheck.class) //수정시에만 적용
      private Long id;
      
      @NotBlank(groups = {SaveCheck.class, UpdateCheck.class})
      private String itemName;
      
      @NotNull(groups = {SaveCheck.class, UpdateCheck.class})
      @Range(min = 1000, max = 1000000, groups = {SaveCheck.class,
                                                  UpdateCheck.class})
      private Integer price;
      
      @NotNull(groups = {SaveCheck.class, UpdateCheck.class})
      @Max(value = 9999, groups = SaveCheck.class) //등록시에만 적용
      private Integer quantity;
      ...
  ```

  ```java
  @PostMapping("/{itemId}/edit")
  public String editV2(@PathVariable Long itemId, @Validated(UpdateCheck.class)
                       @ModelAttribute Item item, BindingResult bindingResult) {
      //...
  }
  ```

  - 수정할 때는 `UpdateCheck`만 적용
  - 등록할 때는 `SaveCheck`만 적용
  - 전반적으로 복잡도가 올라감
  - 참고
    - `@Valid`에는 `groups`를 적용할 수 있는 기능이 없어서 `@Validated`를 사용해야 함
  - 실무에서는 잘 사용하지 않음
    - 부가 데이터도 함께 넘어오기 때문



- Form 전송 객체 분리
  - 보통 엔티티를 직접 전달받지 않고 복잡한 폼의 데이터 컨트롤러까지 전달할 별도의 객체를 만들어서 전달
  - 폼 데이터 전달을 위한 별도의 객체 사용
    - `HTML Form -> ItemSaveForm -> Controller -> Item 생성 -> Repository`
    - 장점 :  별도의 폼 객체를 사용해서 데이터를 전달 받을 수 있다. 보통 등록과, 수정용으로 별도의 폼 객체를 만들기 때문에 검증이 중복되지 않는다.
    - 단점 :  폼 데이터를 기반으로 컨트롤러에서 Item 객체를 생성하는 변환 과정이 추가된다.
  - Q: 등록, 수정용 뷰 템플릿이 비슷한데 합치는게 좋을까요?
    - 어설프게 합치면 수 많은 분기문(등록일 때, 수정일 때) 때문에 나중에 유지보수에서 고통을 맛본다.
    -  어설픈 분기문들이 보이기 시작하면 분리해야 할 신호이다.



- `@ModelAttribute` vs `@RequestBody`
  - `@ModelAttribute`
    - 필드 단위로 정교하게 바인딩이 적용된다.
    - 특정 필드가 바인딩 되지 않아도 나머지 필드는 정상 바인딩 되고, `Validator`를 사용한 검증도 적용할 수 있다. 
  - `@RequestBody`
    - `HttpMessageConverter` 단계에서 `JSON` 데이터를 객체로 변경하지 못하면 이후 단계 자체가 진행되지 않고 예외가 발생
    - 컨트롤러도 호출되지 않고, `Validator`도 적용할 수 없다
  - 참고
    - `HttpMessageConverter`(`JSON` -> 객체 생성) 단계에서 실패하면 예외가 발생