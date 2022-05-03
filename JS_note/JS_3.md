### AJAX

- 서버통신 위해서 `XMLHttpRequest` 객체 활용
- 페이지 일부 업데이트가능 -> **비동기성**
- 주요 특징
  - 새로고침 없이 서버에 요청
  - 서버로부터 데이터를 받고 작업 수행

- console에서 `Log XMLHttpRequests` 체크



### Asynchronous JavaScript

- 동기식

- 비동기식
  - 병렬적 Task 수행
  - non-blocking
  - JS는 single-thread(call stack 하나)

- Threads
  - 프로그램이 작업을 완료하기 위해 사용할 수 있는 단일 프로세스
  - 한번에 하나의 작업

- `setTimeout(콜백함수, 시간)`
- Concurrency model
  - Call Stack
  - Web API
  - Task Queue
  - Event Loop
- Web Apis(Browser Apis라고 보면 됨)





### Callback function

- 다른 함수에 인자로 전달된 함수
- 동기식, 비동기식 모두 사용



### Async callbacks

- 백그라운드에서 코드 실행을



### callback Hell

- 연쇄 비동기 작업
- 해결하기
  - 코드의 깊이를 얕게 유지
  - 모듈화
  - 모든 단일 오류 처리
  - **Promise 콜백 방식 사용**





### Promise

- Promise object
  - 성공에 대한 약속
    - `.then(callback)`
    - 여러개 추가 가능(Chaning)
  - 실패에 대한 약속
    - `.catch(callback)`
- 엄격한 순서로 호출



### Axios

