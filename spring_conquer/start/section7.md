## AOP

- **AOP가 필요한 상황**
  - 모든 메소드의 호출 시간을 측정하고 싶다면?
- **AOP 적용**
  - `Aspect Oriented Programming`
  - 원하는 곳에 공통 관심 사항 적용
  - `@Aspect` , 스프링빈으로 등록 필요
  - 어디에 적용할지 타게팅 필요
    - ex) `@Around("execution(* hello.hellospring..*(..))")`
      - hellospring 하위 목록 모두 적용
  - 핵심 관심 사항과 공통 관심 사항을 깔끔하게 분리가능
  - AOP 적용 후 의존 관계
    - `Controller`가 호출하면 `Proxy Service`(가짜)호출
    - `joinPoint.proceed()`가 호출되면 실제 `Service` 호출