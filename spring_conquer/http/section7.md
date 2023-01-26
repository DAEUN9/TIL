## HTTP 헤더1 - 일반 헤더

- **HTTP 헤더 개요**
  - 과거 헤더 분류 - 폐기됨
    - General 헤더
    - Request 헤더
    - response 헤더
    - Entity 헤더
      - 엔티티 본문의 데이터를 해석할 수 있는 정보
      - 데이터 유형, 데이터 길이, 압축 정보 등
  - 최근 헤더
    - 엔티티 -> 표현
    - 메시지 본문 = 페이로드
    - 표현 = 표현 메타데이터 + 표현 데이터
- **표현**
  - 표현 헤더는 전송, 응답 둘 다 사용
  - `Content-Type` : 표현 데이터의 형식 설명
  - `Content-Encoding` : 표현 데이터 인코딩
    - 데이터를 읽는 쪽에서 인코딩 헤더의 정보로 압축 해제
  - `Content-Language` : 표현 데이터의 자연 언어
    - ex) ko, en, en-US
  - `Content-Length` : 바이트 단위
    - 전송 코딩을 사용할 때 사용하면 안됨
- **콘텐츠 협상**
  - 클라이언트가 선호하는 표현 요청
  - 협상과 우선순위1
    - `Quality Values(q)` 값 사용
    - 0~1, 클수록 높은 우선순위
    - 생략하면 1
  - 협상과 우선순위2
    - 구체적인 것이 우선
    - `Accept: text/*, text/plain, text/plain;format=flowed, */*`
  - 협상과 우선순위3
    - 구체적인 것을 기준으로 미디어 타입을 맞춤
  - 협상 헤더는 요청시에만 사용
- **전송 방식**
  - 단순 전송
  - 압축 전송
  - 분할 전송
    - 마지막엔 `\r\n`으로 표현
    - `Content-Length`를 보내면 안됨
  - 범위 전송
- **일반 정보**
  - `From` : 유저 에이전트의 이메일 정보, 잘안씀
  - `Referer` : 이전 웹페이지 주소
    - 유입경로 분석 가능
    - 요청에서 사용
    - 참고 : referer는 단어 referrer의 오타
  - `User-Agent` : 클라이언트 애플리케이션 정보(웹 브라우저 정보 등등)
    - 어떤 종류의 브라우저에서 장애가 발생하는지 파악 가능
    - 요청에서 사용
  - `Server` : 요청을 처리하는 ORIGIN 서버의 소프트웨어 정보
  - `Date` : 응답에서 사용
- **특별한 정보**
  - `Host` : 요청한 호스트 정보(도메인)
    - 요청에서 사용, 필수
  - `Location` : 페이지 리다이렉션
    - `3xx`, `201 Created`(새로운 리소스 URI 생성)에서도 사용 가능
  - `Allow` : 허용 가능한 HTTP 메서드
  - `Retry-After` : 유저 에이전트가 다음 요청을 하기까지 기다려야 하는 시간
    - `503`과 함께 보냄
- **인증**
  - `Authorization` : 클라이언트 인증 정보를 서버에 전달
    - `Authentication: Basic xxxxxxxxxxxx`
  - `WWW-Authenticate` : 리소스 접근시 필요한 인증 방법 정의
    - `401 Unauthorized` 응답과 함께 사용
- **쿠키**
  - `Set-Cookie` : 웹 브라우저 안 쿠키 저장소에 정보 저장
    - 사용처
      - 사용자 로그인 세션 관리
      - 광고 정보 트래킹
  - `Cookie` : 서버로 보내는 모든 요청에 쿠키 정보 자동 포함
    - 네트워크 트래픽 추가 유발 떄문에 최소한 정보만 사용
    - 웹 스토리지 : 서버에 전송하지 않고 웹 브라우저 내부에 데이터 저장 
  - 보안에 민감한 데이터는 저장하면 안됨
  - 쿠키 - 생명주기
    - `expires=` : 만료일이 되면 쿠키 삭제
    - `max-age=` : 0이나 음수를 지정하면 쿠키 삭제
    - 세션 쿠키 : 만료 날짜를 생략하면 브라우저 종료시 까지만 유지
    - 영속 쿠키: 만료 날짜를 입력하면 해당 날짜까지 유지
  - 쿠키 - 도메인
    - `domain=`
    - 명시 : 명시한 문서 기준 도메인 + 서브 도메인 포함
    - 생략: 현재 문서 기준 도메인만 적용
  - 쿠키 - 경로
    - `path=` : 이 경로를 포함한 하위 경로 페이지만 쿠키 접근
    - 일반적으로 `path=/` 루트로 지정
  - 쿠키 - 보안
    - `Secure=` : https인 경우에만 전송
      - 쿠키는 원래 http, https 구분x
    - `HttpOnly=` : 자바스크립트에서 접근 불가
      - XSS 공격 방지
      - HTTP 전송에만 사용
    - `SameSite=` : 요청 도메인과 쿠키에 설정된 도메인이 같은 경우만 쿠키 전송
      - XSRF 공격 방지 