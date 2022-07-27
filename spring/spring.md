- controller
  - 모든 요청은 컨트롤러를 통해 진행



- `@PathVariable`
  - URI에 담긴 중괄호 위치의 값을 받음

- `@RequestParam`
  - ?를 기준으로 `키=값` 형태로 구성된 요청 전송
- `map객체`
  - 쿼리스트링에 어떤 값이 들어올지 모름

- `DTO`
  - 매개변수로 사용되는 데이터 객체
  - 별도의 로직 x
  - 전달하고하는 필드 객체 선언, getter/setter 구현
- `@RequestBody`
  - HTTP의 Body내용을 해당 어노테이션이 지정된 객체에 매핑
  - 자동으로 Jason과 같은 형식으로 반환
- `ResponseEntity`
  - 서버에 들어온 요청에 대해 응답 데이터를 구성, 전달
  - HttpEntity로부터 Header와 Body를 가지고 자체적으로 HttpStatus 구현
- `@Transient`
  - 엔티티 클래스에 선언된 필드지만 DB에는 필요 없을 경우



- 리포지토리
  - 엔티티가 생성한 DB 접근에 도움
  - 접근하려는 테이블과 매핑되는 엔티티에 대한 인터페이스 생성
  - JpaRepository를 상속받음
  - 메서드 이름은 첫단어 제외 이후 단어들의 첫글자 대문자
- `@Transactional`
  - 작업을 마칠경우 자동으로 flush()메서드 실행
  - 변경 감지되면 레코드 업데이트 쿼리 실행
- 서비스 클래스
  - 핵심기능 제공
- 빌더 메서드
  - 필요한 데이터만 설정 가능
- 롬복 주요 어노테이션
  - Getter/Setter
  - NoArgsConstructor
    - 매개변수가 없는 생성자 자동 생성
  - AllArgsConstructor
    - 모든 필드를 매개변수로 갑는 생성자 자동생성
  - RequiredArgsConstructor: 필드중 final이나 @NotNull이 설정된 변수를 매개변수로 갖는 생성자 자동 생성
  - ToString
    - 필드의 값을 문자열로 조합해서 리턴
    - exclude 속성을 사용해 특정 필드 자동 생성제외가능
  - EqualsAndHashCode
    - 객체의 동등성과 동일성을 비교하는 연산 메서드 생성
    - 부모까지 비교하려면 callSuper속성
  - Data
    - 모두 포괄하는 어노테이션