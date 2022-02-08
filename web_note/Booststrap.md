# Booststrap

### CDN

> Content Delivery(Distribution) Network
>
> 컨텐츠를 효율적으로 전달하기 위해 여러 노드에 가진 네트워크에 데이터를 제공하는 시스템



### spacing

| class name | rem  | px   |
| ---------- | ---- | ---- |
| m-1        | 0.25 | 4    |
| m-2        | 0.5  | 8    |
| m-3        | 1    | 16   |
| m-4        | 1.5  | 24   |
| m-5        | 3    | 48   |

- `.mx-0`

```css
.mx-0 {
    margin-right: 0 !important;
    margin-left: 0 !important;
}
```

- `.mx-auto`: 수평 중앙 정렬

```css
.mx-auto {
    margin-right: auto !important;
    margin-left: auto !important;
}
```

- `.py-0`

```css
.py-0 {
    padding-top: 0 !important;
    padding-bottom: 0 !important;
}
```



| t    | top         |
| ---- | ----------- |
| b    | bottom      |
| s    | left        |
| e    | right       |
| x    | left, right |
| y    | top, bottom |

- `m` = margin
- `p` = padding





### color

`.bg-color`



### Responsive Web Design

> 별도의 기술 이름이 아닌 웹 디자인에 대한 접근 방식, 반응형 레이아웃 작성에 도움이 되는 사례들의 모음 등을 기술하는데 사용되는 용어





### Grid system (web design)

> 요소들의 디자인과 배치에 도움을 주는 시스템

- 기본 요소
  - Column: 실제 컨텐츠를 포함하는 부분
  - Gutter: 칼럼과 칼럼 사이의 공간 (사이 간격)
  - Container: Column들을 담고 있는 공간
- flexbox로 제작, container, rows, column으로 컨텐츠를 배치하고 정렬
- 반드시 기억해야 할 2가지!
  - 12개의 column
  - 6개의 grid breakpoints

### breakpoints

- `xs`(phones): auto, <576px
- `sm`(tablets): >=576px
- `md`(desktop): >=768px
- `lg`(larger desktops): >=992px
- `xl`: >=1200px
- `xxl`: <=1400px

### offset

> 기존 위치에서 이동

