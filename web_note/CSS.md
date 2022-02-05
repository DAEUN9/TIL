# CSS

> Cascading Style Sheets
>
> 스타일을 지정하기 위한 언어



### CSS 구문 - 용어 정리

```css
h1 # 선택자{
    color: blue; # 선언
    font-size: 15px; # 속성: 값;
}
```

- CSS 구문은 선택자를 통해 스타일을 지정할 HTML 요소를 선택
- 중괄호 안에는 속성과 값, 하나의 쌍으로 이루어진 선언을 진행
- 각 쌍은 선택한 요소의 속성, 속성에 부여할 값을 의미
  - 속성 (Property) : 어떤 스타일 기능을 변경할지 결정
  - 값 (Value) : 어떻게 스타일 기능을 변경할지 결정



### CSS 정의 방법

- 인라인(inline)
  - html 파일의 해당 태그에 직접 style 속성을 활용

- 내부 참조(embedding) - `<style>`
  - html 파일의 `<head>` 태그 내에 `<style>`에 지정
- 외부 참조(link file) - 분리된 CSS 파일
  - 외부 CSS 파일을 `<head>`내 `<link>`를 통해 불러오기





### CSS with 개발자 도구

- styles : 해당 요소에 선언된 모든 CSS
- computed: 해당 요소에 최종 계산된 CSS





### 선택자(Selector) 유형

- 기본 선택자
  - 전체 선택자, 요소 선택자
  - 클래스 선택자, 아이디 선택자, 속성 선택자
- 결합자(Combinators)
  - 자손 결합자, 자식 결합자
  - 일반 형제 결합자, 인접 형제 결합자
- 의사 클래스/요소(Pseudo Class)
  - 링크, 동적 의사 클래스
  - 구조적 의사 클래스, 기타 의사 클래스, 의사 엘리먼트, 속성 선택자

```html
<style>
    /* 전체 선택자 */
    * {
        color: red;
    }
    
    /* 요소 선택자 */
    h2 {
        color: orange;
    }
    
    h3,
    h4 {
        font=size: 10px;
    }
    
    /* 클래스 선택자 */
    .green {
        color: green;
    }
    
    /* id 선택자 */
    #purple {
        color: purple;
    }
    
    /* 자식 결합자 */
    .box > p {
        font-size: 30px;
    }
    
    /* 자손 결합자 */
    .box p {
        color: blue;
    }
</style>
```





### CSS 적용 우선순위

1. 중요도 (importance) - 사용시 주의
   - !important
2. 우선 순위 (Specificity)
   - 인라인 > id > class, 속성, pseudo-class > 요소, pseudo-element
3. CSS 파일 로딩 순서





### CSS 상속

- 속성 중에는 상속이 되는 것과 되지 않는 것들이 있다.

  - 상속 되는 것 예시

    ex) Text 관련 요소(font, color, text-align), opacity, visibility 등

  - 상속 되지 않는 것 예시

​				ex) Box model 관련 요소, position 관련 요소 등





### 크기 단위

- `px` (픽셀)
  - 고정적인 단위
- `%`
  - 가변적인 레이아웃에서 주로 사용
- `em`
  - 상속의 영향을 받음
  - 배수 단위, 요소에 지정된 사이즈에 상대적인 사이즈를 가짐
- `rem`
  - 상속의 영향을 받지 않음
  - 최상위 요소(html)의 사이즈를 기준으로 배수 단위를 가짐

- `viewport`
  - 웹 페이지를 방문한 유저에게 바로 보이게 되는 웹 컨텐츠의 영역 (디바이스 화면)
  - 디바이스의 viewpoint를 기준으로 상대적인 사이즈가 결정됨
  - vw, vh, vmin, vmax





### 색상 단위

- 색상 키워드
  - 대소문자 구분X
  - 특정 색을 직접 글자로 나타냄

- RGB 색상
  - 16진수 표기법 혹은 함수형 표기법을 사용해서 특정 색을 표현
  - '#' + 16진수 표기법
  - rgb() 함수형 표기법
- HSL 색상
  - 색상, 채도, 명도를 통해 특정 색을 표현

- a는 alpha(투명도)





### 결합자 (Combinators)

- 자손 결합자

  - selectorA 하위의 모든 selectorB 요소

    ```css
    div span {
        color: red;
    }
    ```

    

- 자식 결합자

  - selectorA 바로 아래의 selectorB 요소

    ```css
    div > span {
        color: red;
    }
    ```

    

- 일반 형제 결합자

  - selectorA의 형제 요소 중 뒤에 일치하는 selectorB 요소를 모두 선택

    ```css
    p ~ span {
        color: red;
    }
    ```

    

- 인접 형제 결합자

  - selectorA의 형제 요소 중 바로 뒤에 위치하는 selectorB 요소를 선택

    ```css
    p + span {
        color: red;
    }
    ```



### CSS 원칙 1

**모든 요소는 네모(박스모델)이고, 위에서부터 아래로, 왼족에서 오른쪽으로 쌓인다.**





### Box model

- 하나의 박스는 네 부분(영역)으로 이루어짐
  - `content` : 글이나 이미지 등 요소의 실제 내용
  - `padding` : 테두리 안쪽의 내부 여백 요소에 적용된 배경색, 이미지는 padding까지 적용
  - `border` : 테두리 영역
  - `margin` : 테두리 바깥의 외부 여백. 배경색을 지정할 수 없다.

### Box model 구성(margin/padding)

```css
.margin-1 {
    margin: 10px;
}

# 상하 좌우
.margin-2 {
    margin: 10px 20px;
}

# 상 좌우 하
.margin-3 {
    margin: 10px 20px 30px;
}

# 상 우 하 좌 (시계방향)
.margin-4 {
    margin: 10px 20px 30px 40px;
}
```

```css
.border{
    border-width: 2px;
    border-style: dashed;
    border-color: black;
}

# shorthand
.border{
    border: 2px dashed black;
}
```

### box-sizing

- 기본적으로 모든 요소의 box-sizing은 content-box
  - Padding을 제외한 순수 contents 영역만을 box로 지정
- 다만, 우리가 일반적으로 영역을 볼 때는 border까지의 너비를 100px 보는 것을 원함
  - 그 경우 box-sizing을 border-box으로 설정





### CSS 원칙 2

**display에 따라 크기와 배치가 달라진다.**





### 대표적으로 활용되는 display

- `display: block`
  - 줄 바꿈이 일어나는 요소
  - 화면 크기 전체의 가로 폭을 차지한다.
  - 블록 레벨 요소 안에 인라인 레벨 요소가 들어갈 수 있음.
- `display: inline`
  - 줄 바꿈이 일어나지 않는 행의 일부 요소
  - content 너비만큼 가로 폭을 차지한다.
  - width, height, margin-top, margin-bottom을 지정할 수 없다.
  - 상하 여백은 line-height로 지정한다.
- `display: inline-block`
  - block과 inline 레벨 요소의 특징을 모두 가짐
  - inline처럼 한 줄에 표시 가능하고, block처럼 width, height, margin 속성을 모두 지정할 수 있음
- `display: none`
  - 해당 요소를 화면에 표시하지 않고, 공간조차 부여X
  - 이와 비슷한 `visibility: hidden`은 해당 요소가 공간은 차지하나 화면에 표시만 하지 않는다.





### 블록 레벨 요소와 인라인 레벨 요소

- 대표적인 블록 레벨 요소
  - div / ul, ol, li / p / hr / form 등
  - block의 기본 너비는 가질 수 있는 너비의 100%
  - 너비를 가질 수 없다면 margin 자동 부여
- 대표적인 인라인 레벨 요소
  - span / a / img / input, label / b, em, i, strong 등
  - inline의 기본 너비는 컨텐츠 영역만큼





### 속성에 따른 수평 정렬

```css
margin-right: auto;
# 같다
text-align: left;

margin-left: auto;
# 같다
text-align: right;

margin-right: auto;
margin-left: auto;
# 같다
text-align: center;
```





### CSS position

> 문서 상에서 요소의 위치를 지정

- `static`: 모든 태그의 기본 값(기준 위치)
  - 일반적인 요소의 배치 순서에 따름(좌측 상단)
  - 부모 요소 내에서 배치될 때는 부모 요소의 위치를 기준으로 배치
- 아래는 좌표 프로퍼티(top, bottom, left, right)를 사용하여 이동 가능
  - `relative`: 상대위치
    - **자기 자신의 static 위치를 기준으로 이동** (normal flow 유지)
    - 레이아웃에서 요소가 차지하는 공간은 static 일 때와 같음 (normal position 대비 offset)
  - `absolute`: 절대 위치
    - 요소를 일반적이니 문서 흐름에서 제거 후 레이아웃에 공간을 차지하지 않음 (normal flow에서 벗어남)
    - static이 아닌 **가장 가까이 있는 부모/조상 요소를 기준으로 이동** (없는 경우 body)
    - 다음블록 요소가 좌측 상단으로 붙음
  - `fixed`: 고정 위치
    - 요소를 일반적인 문서 흐름에서 제거 후 레이아웃에 공간을 차지하지 않음 (normal flow에서 벗어남)
    - 부모 요소와 관계없이 **viewport를 기준으로 이동**





### CSS 원칙 3

**position으로 위치의 기준을 변경**

