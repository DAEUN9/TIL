## 타임리프 스프링 통합

- 타임리프 설정
  - `implementation 'org.springframework.boot:spring-boot-starter-thymeleaf'`
  - 관련 설정을 변경하고 싶으면 `application.properties`에 추가

- 입력 폼 처리

  - `th:object="${item}"` : `<form>`에서 사용할 객체 지정

    - 선택 변수 식 (`*{...}`)을 적용할 수 있음

  - `th:field="*{itemName}"`

    - `${item.itemName}` 과 같다
    - `th:field` 는 `id` , `name` , `value` 속성을 모두 자동으로 만들어 준다
    - `id` : `th:field` 에서 지정한 변수 이름과 같다.
      - `id="itemName"`
    - `name` : `th:field` 에서 지정한 변수 이름과 같다.
      - `name="itemName"`
    - `value` : `th:field` 에서 지정한 변수의 값을 사용한다
      - `value=""`

  - 렌더링 전

    ```html
    <input type="text" id="itemName" th:field="*{itemName}" class="form-control" placeholder="이름을 입력하세요">
    ```

  - 렌더링 후

    ```html
    <input type="text" id="itemName" class="form-control" placeholder="이름을 입력하세요" name="itemName" value="">
    ```

    

- 체크 박스 - 단일1

  ```html
  <div class="form-check">
    <input type="checkbox" id="open" name="open" class="form-check-input">
    <label for="open" class="form-check-label">판매 오픈</label>
  </div>
  ```

  - 체크박스를 체크하면 `open=on`이라는 값이 넘어가고
  - 스프링은 `on`을 true로 변경
  - 주의 - 체크 박스를 선택하지 않을 때
    - HTML에서 체크 박스를 선택하지 않고 폼을 전송하면 `open` 이라는 필드 자체가 서버로 전송되지 않는다
    - 체크를 해제해도 아무 값도 넘어가지 않음
    - 히든 필드를 하나 만들어서, `_open`처럼 언더바를 넣어서 전송
    - 이 경우 스프링 MVC는 체크를 해제했다고 판단
    - `<input type="hidden" name="_open" value="on"/>`

  ```html
  <div class="form-check">
    <input type="checkbox" id="open" name="open" class="form-check-input">
    <input type="hidden" name="_open" value="on"/>
    <label for="open" class="form-check-label">판매 오픈</label>
  </div>
  ```

  - 체크 박스 체크 
    - `open=on&_open=on`
    - `_oepn` 무시
  - 체크 박스 미체크
    - `_open=on`

  

  - 체크박스 - 단일2

    - 체크 박스 코드

      ```html
      <div>판매 여부</div>
      <div>
       <div class="form-check">
       <input type="checkbox" id="open" th:field="*{open}" class="form-check-input">
       <label for="open" class="form-check-label">판매 오픈</label>
       </div>
      </div>
      ```

    - 타임리프 체크 박스 HTML 생성 결과

      ```html
      <div>판매 여부</div>
      <div>
       <div class="form-check">
       <input type="checkbox" id="open" class="form-check-input" name="open"value="true">
       <input type="hidden" name="_open" value="on"/>
       <label for="open" class="form-check-label">판매 오픈</label>
       </div>
      </div>
      ```

    - hidden 필드를 자동으로 생성해줌
    - 체크 확인
      - 체크 박스에서 판매 여부를 선택해서 저장하면. `checked` 속성이 추가됨
      - `checked="checked"`

  

- 체크 박스 - 멀티

  - `@ModelAttribute`

    - 반복해서 데이터를 담아서 보여주어야 함
    - 컨트롤러에 있는 별도의 메서드에 적용 가능
    - static처럼 미리 생성하고 공유해서 쓰는 것이 효율적
    - 해당 컨트롤러를 요청 할 때 반환 값이 자동으로 모델에 담김

    ```java
    @ModelAttribute("regions")
    public Map<String, String> regions() {
        Map<String, String> regions = new LinkedHashMap<>();
        regions.put("SEOUL", "서울");
        regions.put("BUSAN", "부산");
        regions.put("JEJU", "제주");
        return regions;
    }
    ```

  - `th:for="${#ids.prev('regions')}"`

    - 멀티 체크박스들의 `name`은 같아도 되지만 `id`는 모두 달라야 함
    - 체크박스를 `each`루프 안에서 반복해서 만들 때 임의로 숫자를 뒤에 붙여줌
      - `id=regions1`, `id=regions2` ...

  - 서울, 부산 선택 로그

    ```
    regions=SEOUL&_regions=on&regions=BUSAN&_regions=on&_regions=on
    ```

  - 지역 선택X

    ```
    _regions=on&_regions=on&_regions=on
    ```

  - 타임리프는 `th:field` 에 지정한 값과 `th:value` 의 값을 비교해서 체크를 자동으로 처리

    ```html
    <div>등록 지역</div>
    <div th:each="region : ${regions}" class="form-check form-check-inline">
        <input type="checkbox" th:field="${item.regions}" th:value="${region.key}"
               class="form-check-input" disabled>
        <label th:for="${#ids.prev('regions')}"
               th:text="${region.value}" class="form-check-label">서울</label>
    </div>
    ```

    

- 라디오 버튼

  - `ENUM`을 사용
  - `ItemType.values()` :해당 ENUM의 모든 정보를 배열로 반환한다.
    - 예) `[BOOK, FOOD,  ETC]`

  ```html
  <div>상품 종류</div>
  <div th:each="type : ${itemTypes}" class="form-check form-check-inline">
      <input type="radio" th:field="*{itemType}" th:value="${type.name()}"
             class="form-check-input">
      <label th:for="${#ids.prev('itemType')}" th:text="${type.description}"
             class="form-check-label">
          BOOK
      </label>
  </div>
  ```

  - 실행 로그

    ```
    item.itemType=FOOD: 값이 있을 때
    item.itemType=null: 값이 없을 때
    ```

  - ENUM 직접 사용하기
    - `<div th:each="type : ${T(hello.itemservice.domain.item.ItemType).values()}">`
    - ENUM의 패키지 위치가 변경되거나 할때 자바 컴파일러가 타임리프까지 컴파일 오류를 잡을 수 없음
    - 비추천



- 셀렉트 박스

  ```html
  <select th:field="*{deliveryCode}" class="form-select">
      <option value="">==배송 방식 선택==</option>
      <option th:each="deliveryCode : ${deliveryCodes}" th:value="${deliveryCode.code}"
              th:text="${deliveryCode.displayName}">FAST</option>
  </select>
  ```

  - 생성된 html

    ```html
    <select class="form-select" id="deliveryCode" name="deliveryCode">
        <option value="">==배송 방식 선택==</option>
        <option value="FAST">빠른 배송</option>
        <option value="NORMAL">일반 배송</option>
        <option value="SLOW">느린 배송</option>
    </select>
    ```

  - `th:field`와 `th:value`를 비교해서 셀렉트 선택

    - `selected="selected"`

    ```html
    <select class="form-select" id="deliveryCode" name="deliveryCode">
        <option value="">==배송 방식 선택==</option>
        <option value="FAST" selected="selected">빠른 배송</option>
        <option value="NORMAL">일반 배송</option>
        <option value="SLOW">느린 배송</option>
    </select>
    ```

    

