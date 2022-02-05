# HTML

> Hyper Text Markup Language
>
> 웹 페이지를 작성(구조화) 하기 위한 언어





### 현재의 웹 표준

```
W3C, WHATWG
```





### 크롬 개발자 도구

- 주요 기능
  - `Elements` - DOM 탐색 및 CSS 확인 및 변경
    - Styles - 요소에 적용된 CSS 확인
    - Computed - 스타일이 계산된 최종 결과
    - Event Listeners - 해당 요소에 적용된 이벤트 (JS)
  - Sources, Network, Performance, Application, Security, Audits 등



### Markup Language

- 태그 등을 이용하여 문서나 데이터의 구조를 명시하는 언어
  - ex) HTML, Markdown





### HTML 기본 구조

- `html`: 문서의 최상위(root) 요소
- `head`: 문서 메타데이터 요소
  - 문서 제목, 인코딩, 스타일, 외부 파일 로딩 등
  - 일반적으로 브라우저에 나타나지 않는 내용
- `body`: 문서 본문 요소
  - 실제 화면 구성과 관련된 내용

```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>
<body>
    
</body>
</html>
```





### head 예시

- `<title>` : 브라우저 상단 타이틀
- `<meta>` : 문서 레벨 메타데이터 요소
- `<link>` : 외부 리소스 연결 요소 (CSS 파일, favicon 등)
- `<script>` : 스크립트 요소 (JavaScript 파일/코드)
- `<style>` : CSS 직접 작성

```html
<head>
    <title>HTML 수업</title>
    <meta charset="UTF-8">
    <link href="style.css" rel="stylesheet">
    <script src="javascript.js"></script>
    <style>
    p {
   		color: black;
        }
    </style>
</head>
```

#### Open Graph Protocol

- 메타 데이터를 표현하는 새로운 규약
  - HTML 문서의 메타 데이터를 통해 문서의 정보를 전달
  - 메타정보에 해당하는 제목, 설명 등을 쓸 수 있도록 정의





### DOM(Document Object Model) 트리

- 텍스트 파일인 HTML 문서를 브라우저에서 렌더링 하기 위한 구조
  - HTML 문서에 대한 모델을 구성
  - HTML 문서 내의 각 요소에 접근 / 수정에 필요한 프로퍼티와 메서드 제공





### 요소(element)

> 태그와 내용(contents) 로 구성

```html
<h1>
    contents
</h1>
```

- 내용이 없는 태그들
  - br, hr, img, input, link, meta
- 요소는 중첩(nested)될 수 있음





### 속성(attribute)

> 태그별로 사용할 수 있는 속성 다름

```html
<a href="https://google.com"></a>
# 속성명(href)/ 속성값(주소)
# 공백X 쌍따옴표 사용!
```

- 요소는 속성을 가질 수 있으며, 경로나 크기와 같은 추가적인 정보 제공
- 태그와 상관없이 사용 가능한 속성(HTML Global Attribute)들도 있음





### HTML Global Attribute

- 모든 HTML 요소가 공통으로 사용할 수 있는 대표적인 속성(몇몇 요소에는 아무 효과도 없음)
  - `id` : 문서 전체에서 유일한 고유 식별자 지정
  - `class` : 공백으로 구분된 해당 요소의 클래스 목록
  - `data-*` : 페이지에 개인 사용자 정의 데이터를 저장하기 위해 사용
  - `style` : inline 스타일
  - `title` : 요소에 대한 추가 정보 지정
  - `tabindex` : 요소의 탭 순서





### 시맨틱 태그

> 기존 영역을 의미하는 div 태그를 대체, 의미론적 요소를 담은 태그

- 대표적인 태그 목록
  - `header` : 문서 전체나 섹션의 헤더(머리말 부분)
  - `nav` : 네비게이션
  - `aside` : 사이드에 위치한 공간
  - `section` : 문서의 일반적인 구분, 컨텐츠의 그룹을 표현
  - `article` : 문서, 페이지, 사이트 안에서 독립적으로 구분되는 영역
  - `footer` : 문서 전체나 섹션의 푸터(마지막 부분)
- None semantic 요소는 div, span 등이 있으며 h1, table 태그들도 시맨틱 태그로 볼 수 있음
- 단순히 구역을 나누는 것 뿐만 아니라 '의미'를 가지는 태그들을 활용하기 위한 노력
- 요소의 의미가 명확해지기 때문에 코드의 가독성을 높이고 유지보수를 쉽게 함
- 검색엔진최적화(SEO)를 위해서 메타태그, 시맨틱 태그 등을 통한 마크업을 효과적으로 활용 해야함





### 텍스트 요소

| 태그                               | 설명                                                         |
| :--------------------------------- | :----------------------------------------------------------- |
| `<a></a>`                          | href 속성을 활용하여 다른 URL로 연결하는 하이퍼링크 생성     |
| `<b></b>`<br />`<strong></strong>` | 굵은 글씨 요소<br />중요한 강조하고자 하는 요소 (보통 굵은 글씨로 표현) |
| `<i></i>`<br />`<em></em>`         | 기울임 글씨 요소<br />중요한 강조하고자 하는 요소 (보통 기울임 글씨로 표현) |
| `<br>`                             | 텍스트 내에 줄 바꿈 생성                                     |
| `<img>`                            | src 속성을 활용하여 이미지 표현                              |
| `<span></span>`                    | 의미 없는 인라인 컨테이너                                    |





### 그룹 컨텐츠

| 태그                         | 설명                                                         |
| :--------------------------- | :----------------------------------------------------------- |
| `<p><p/>`                    | 하나의 문단                                                  |
| `<hr>`                       | 문단 레벨 요소에서의 주제의 분리를 의미하며<br />수평선으로 표현됨 (A Horizontal Rule) |
| `<ol></ol>`<br />`<ul></ul>` | 순서가 있는 리스트 (ordered)<br />순서가 없는 리스트 (unordered) |
| `<pre></pre>`                | HTML에 작성한 내용을 그대로 표현.<br />보통 고정폭 글꼴이 사용되고 공백문자를 유지 |
| `<blockquote></blockquote>`  | 텍스트가 긴 인용문<br />주로 들여쓰기를 한 것으로 표현됨     |
| `<div></div>`                | 의미 없는 블록 레벨 컨테이너                                 |





### table

> 각 영역을 명시하기 위해 `<thead>` `<tbody>` `<tfoot>` 요소를 활용

- `<tr>`으로 가로 줄을 구성하고 내부에는 `<th>` 혹은 `<td>`로 셀을 구성
- colspan, rowspan 속성을 활용해 셀 병합
  - colspan="2" 이면 칼럼 2개를 셀 병합
- `<caption>`을 통해 표 설명 또는 제목을 나타냄





### form

> 정보(데이터)를 서버에 제출하기 위한 영역

- `<form>` 기본 속성
  - `action` : form을 처리할 서버의 URL
  - `method` : form을 제출할 때 사용할 HTTP 메서드 (GET 혹은 POST)
  - `enctype` : method가 post인 경우 데이터의 유형
    - `application/x-www-form-urlencoded` : 기본값
    - `multipart/form-data` : 파일 전송시 (input type이 file인 경우)





### input

> 다양한 타입을 가지는 입력 데이터 유형과 위젯이 제공됨

- `<input>` 대표적인 속성
  - `name` : form control에 적용되는 이름 (이름/값 페어로 전송됨)
  - `value` : form control에 적용되는 값 (이름/값 페어로 전송됨)
  - required, readonly, autofocus, autocomplete, disabled 등

```html
<form action="/serch" method="GET">
    <input type="text" name="q">
</form>
```

### input label

- label을 클릭하여 input 자체의 초점을 맞추거나 활성화 시킬 수 있음
  - 화면리더기에서도 label을 읽어 쉽게 내용 확인
- `<input>`에 id 속성을, `<label>`에는 for 속성을 활용하여 상호 연관

```html
<label for="areement">개인정보 수집에 동의합니다.</label>
<input type="checkbox" name="agreement" id="agreement">
```

### input 유형 - 일반

> 일반적으로 입력을 받기 위해 제공되며 타입별로 HTML기본 검증 혹은 추가 속성을 활용할 수 있음

- `text` : 일반 텍스트 입력
- `password` : 입력 시 값이 보이지 않고 문자를 특수기호(*)로 표현
- `email` : 이메일 형식이 아닌 경우 form 제출 불가
- `number` : min, max, step 속성을 활용하여 숫자 범위 설정 가능
- `file` : accept 속성을 활용하여 파일 타입 지정 가능

### input 유형 - 항목

> 일반적으로 label을 사용하여 내용을 작성하여 항목 중 선택할 수 있는 input을 제공

- 동일 항목에 대하여는 name을 지정하고 선택된 항목에 대한 value를 지정해야 함
  - `checkbox` : 다중 선택
  - `radio` : 단일 선택

### input 유형 - 기타

- 다양한 종류의 input을 위한 picker를 제공
  - `color` : color picker
  - `date` : date picker
- hidden input을 활용하여 사용자 입력을 받지 않고 서버에 전송되어야 하는 값을 설정
  - `hidden` : 사용자에게 보이지 않는 input