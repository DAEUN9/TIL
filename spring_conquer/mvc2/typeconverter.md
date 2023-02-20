## 스프링 타입 컨버터

- 스프링 타입 변환

  - HTTP 요청 파라미터는 모두 문자로 처리

  - MVC 요청 파라미터로 받아서 다른 타입으로 컨버팅 가능

  - 스프링 타입 변환 적용 예

    - 스프링 MVC 요청 파라미터
      - `@RequestParam` , `@ModelAttribute` , `@PathVariable`
    - `@Value` 등으로 YML 정보 읽기
    - XML에 넣은 스프링 빈 정보를 변환
    - 뷰를 렌더링 할 때

  - 컨버터 인터페이스

    - 추가적인 타입 변환

    ```java
    package org.springframework.core.convert.converter;
    
    public interface Converter<S, T> {
     T convert(S source);
    }
    ```

    - 참고 > 과거에는 `PropertyEditor` 라는 것으로 타입을 변환
      - 동시성 문제가 있어서 타입을 변환할 때 마다 객체를 계속 생성해야 하는 단점
    - 지금은 `Converter` 를 사용



- 타입 컨버터 - Converter

  - `@EqualsAndHashCode` 를 넣으면 모든 필드를 사용해서 `equals()` , `hashcode()` 를 생성

  - `org.springframework.core.convert.converter.Converter`

  - 문자를 숫자로 변환하는 타입 컨버터

    ```java
    @Slf4j
    public class StringToIntegerConverter implements Converter<String, Integer> {
        
        @Override
        public Integer convert(String source) {
            log.info("convert source={}", source);
            return Integer.valueOf(source);
        }
        
    }
    
    ```

  - 스프링은 용도에 따라 다양한 방식의 타입 컨버터 제공
    - `Converter`
      - 기본 타입 컨버터
    - `ConverterFactory`
      - 전체 클래스 계층 구조가 필요할 때
    - `GenericConverter`
      - 정교한 구현, 대상 필드의 애노테이션 정보 사용 가능
    - `ConditionalGenericConverter`
      - 특정 조건이 참인 경우에만 실행
  - 스프링은 문자, 숫자, 불린, Enum등 일반적인 타입에 대한 대부분의 컨버터를 기본으로 제공
    - 컨버터의 구현체를 찾아보자



- 컨버전 서비스 - `ConversionService`

  - 개별 컨버터를 모아두고 그것들을 묶어서 편리하게 사용할 수 있는 기능을 제공

  - `ConversionService` 인터페이스

    ```java
    public interface ConversionService {
        boolean canConvert(@Nullable Class<?> sourceType, Class<?> targetType);
        
        boolean canConvert(@Nullable TypeDescriptor sourceType, TypeDescriptor targetType);
        
        <T> T convert(@Nullable Object source, Class<T> targetType);
        
        Object convert(@Nullable Object source,
                       @Nullable TypeDescriptor sourceType, ypeDescriptor targetType);
    }
    ```

  - 테스트

    ```java
    public class ConversionServiceTest {
    
        @Test
        void conversionService() {
            //등록
            DefaultConversionService conversionService = new DefaultConversionService();
            conversionService.addConverter(new StringToIntegerConverter());
            conversionService.addConverter(new StringToIpPortConverter());
    
            //사용
            assertThat(conversionService.convert("10", Integer.class)).isEqualTo(10);
            IpPort ipPort = conversionService.convert("127.0.0.1:8080", IpPort.class);
    		assertThat(ipPort).isEqualTo(new IpPort("127.0.0.1", 8080));
        }
    }
    ```

    - `DefaultConversionService` 는 `ConversionService` 인터페이스를 구현
      - 추가로 컨버터를 등록하는 기능도 제공

  - 등록과 사용 분리

    - 컨버터를 등록할 때는 `StringToIntegerConverter` 같은 타입 컨버터를 명확하게 알아야 한다
    - 컨버터를 사용하는 입장에서는 타입 컨버터를 전혀 몰라도 된다
    - 타입 컨버터들은 모두 컨버전 서비스 내부에 숨어서 제공
    - 타입을 변환을 원하는 사용자는 컨버전 서비스 인터페이스에만 의존

  - 인터페이스 분리 원칙 - ISP

    > 클라이언트가 자신이 이용하지 않는 메서드에 의존하지 않아야 한다

    - `DefaultConversionService` 는 다음 두 인터페이스를 구현했다.
      - `ConversionService` : 컨버터 사용에 초점
      - `ConverterRegistry` : 컨버터 등록에 초점
    - 스프링은 내부에서 `ConversionService` 를 사용해서 타입을 변환
      - `@RequestParam` 같은 곳에서 이 기능을 사용해서 타입을 변환



- 스프링에 Converter 적용하기
  - `WebMvcConfigurer` 가 제공하는 `addFormatters() `를 사용해서 추가하고 싶은 컨버터를 등록
  - 스프링은 내부에서 사용하는 `ConversionService` 에 컨버터를 추가
  - 스프링이 내부에서 수 많은 기본 컨버터들을 제공
  - 컨버터를 추가하면 추가한 컨버터가 기본 컨버터 보다 높은 우선순위
  - 처리 과정
    - `@RequestParam` 은 `@RequestParam` 을 처리하는 `ArgumentResolver` 인 `RequestParamMethodArgumentResolver` 에서 `ConversionService` 를 사용해서 타입을 변환



- 뷰 템플릿에 컨버터 적용하기

  - 타임리프는 `${{...}}` 를 사용하면 자동으로 컨버전 서비스를 사용해서 변환된 결과를 출력
  - 등록한 컨버터들을 사용할 수 있다

  ```html
  <li>${ipPort}: <span th:text="${ipPort}" ></span></li>
  <li>${{ipPort}}: <span th:text="${{ipPort}}" ></span></li>
  ```

  ```html
  • ${ipPort}: hello.typeconverter.type.IpPort@59cb0946
  • ${{ipPort}}: 127.0.0.1:8080
  ```

  - 타임리프의 `th:field` 는 앞서 설명했듯이 `id` , `name` 를 출력하는 등 다양한 기능이 있는데
    - 컨버전 서비스도 함께 적용



- 포맷터 - Formatter

  > 객체를 특정한 포멧에 맞추어 문자로 출력하거나 또는 그 반대의 역할을 하는 것에 특화된 기능

  - `Converter` vs `Formatter`

    - `Converter` 는 범용(객체 -> 객체)
    - `Formatter` 는 문자에 특화(객체 -> 문자, 문자 -> 객체) + 현지화(Locale)
      - `Converter` 의 특별한 버전

  - 포맷터 인터페이스

    ```java
    public interface Printer<T> {
        String print(T object, Locale locale);
    }
    
    public interface Parser<T> {
        T parse(String text, Locale locale) throws ParseException;
    }
    
    public interface Formatter<T> extends Printer<T>, Parser<T> {
    }
    ```

    - `String print(T object, Locale locale)` : 객체를 문자로 변경한다.
    - `T parse(String text, Locale locale)` : 문자를 객체로 변경한다.

  -  스프링은 용도에 따라 다양한 방식의 포맷터를 제공

    - `Formatter`
      - 포맷터
    - `AnnotationFormatterFactory`
      - 필드의 타입이나 애노테이션 정보를 활용할 수 있는 포맷터

  

- 포맷터를 지원하는 컨버전 서비스

  - 포맷터를 지원하는 컨버전 서비스를 사용하면 컨버전 서비스에 포맷터를 추가할 수 있다
  - 내부에서 어댑터 패턴을 사용해서 `Formatter` 가 `Converter` 처럼 동작하도록 지원
  - `FormattingConversionService`
    - 포맷터를 지원하는 컨버전 서비스
  - `DefaultFormattingConversionService`
    - `FormattingConversionService` 에 기본적인 통화, 숫자 관련 몇가지 기본 포맷터를 추가해서 제공
  - `DefaultFormattingConversionService` 상속 관계
    - `FormattingConversionService` 는 `ConversionService` 관련 기능을 상속받기 때문에 결과적으로 컨버터도 포맷터도 모두 등록할 수 있다
    - 사용할 때는 `ConversionService` 가 제공하는 `convert` 를 사용
    - 스프링 부트는
      - `DefaultFormattingConversionService` 를 상속 받은 `WebConversionService` 를 내부에서 사용

  - 우선순위는 컨버터가 우선하므로 포맷터가 적용되지 않고, 컨버터가 적용



- 스프링이 제공하는 기본 포맷터

  - 애노테이션 기반으로 원하는 형식을 지정해서 사용
  - `@NumberFormat`
    - 숫자 관련 형식 지정 포맷터 사용
    - `NumberFormatAnnotationFormatterFactory`
  - `@DateTimeFormat`
    - 날짜 관련 형식 지정 포맷터 사용
    - `Jsr310DateTimeFormatAnnotationFormatterFactory`

  ```java
  @Data
  static class Form {
      @NumberFormat(pattern = "###,###")
      private Integer number;
      @DateTimeFormat(pattern = "yyyy-MM-dd HH:mm:ss")
      private LocalDateTime localDateTime;
  }
  ```

  



- 정리
  - 주의
    - 메시지 컨버터( `HttpMessageConverter` )에는 컨버전 서비스가 적용되지 않는다
    - `HttpMessageConverte`r 의 역할은 HTTP 메시지 바디의 내용을 객체로 변환하거나 객체를 HTTP 메시지 바디에 입력하는 것
    - JSON을 객체로 변환하는 메시지 컨버터는 내부에서 `Jackson` 같은 라이브러리를 사용
    - JSON 결과로 만들어지는 숫자나 날짜 포맷을 변경하고 싶으면 해당 라이브러리가 제공하는 설정을 통해서 포맷을 지정해야 한다
    - 이것은 컨버전 서비스와 전혀 관계가 없다
  - 컨버터와 포매터는 사용할 때, 컨버전 서비스를 통해서 일관성 있게 사용할 수 있다
  - 컨버전 서비스는 `@RequestParam` , `@ModelAttribute` , `@PathVariable` , 뷰 템플릿 등에서 사용할 수 있다