### DOM

- DOM
  - 선택 -> 변경
  - Document 위치에서 시작
  - 선택 관련 메서드
    - `document.querySelector(selector)`
      - 객체 반환
    - `document.querySelectorAll(selector)`
      - 객체리스트 반환
    - query~ 쓰는 이유
      - id, class, tag 등
  - 자식 선택하기
    - `document.querySelector('div > ul')`
  - 변경 관련 메서드
    - `Element.append()`
    - `Element.appendChild()`
    - `document.createElement(selector)`
  - 속성 관련 메서드
    - `Element.setAttribute('attribute_name', 'value')`
    - `Element.getAttribute('attribute_name')`
  - 클래스 추가
    - `Element.classList.add('class_name')`
  - section 내부의 div들 선택
    - `document.querySelectorAll('section div')`
      - forEach 가능

- BOM
- JAVAScript Core
- window.console.log = console.log
- document는 객체(웹화면)





### Event

- 사건의 발생을 알리기 위한 객체
- 특정 이벤트가 발생하면 할 일을 등록한다.
- `EventTarget.addEventListener(type, listener[, options])`
  - 대상에 지정된 이벤트 발생할때마다 함수(일의 단위) 설정
  - type
    - 이벤트 유형
  - listener
    - 동작, 콜백 함수, 일, 명세
  - `confirm(' ~~ ')`
    - 확인 창

- input 태그 기본값은 입력한 값 보이는게 포함