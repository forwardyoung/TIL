# Web

## 💻 웹 사이트의 구성 요소

- HTML ➡️ 구조

- CSS ➡️ 표현

- Javascript ➡️ 동작 

[예시 살펴보기](https://html-css-js.com/)

**🌍 웹 표준**

- 브라우저마다 동작이 약간씩 달라서 문제가 생기는 경우가 많은데, 해결책으로 **웹 표준**이 등장함
- 웹에서 표준적으로 사용되는 기술이나 규칙
- 어떤 브라우저든 웹 페이지가 동일하게 보이도록 함(크로스 브라우징)

- [브라우저별 호환성 체크](https://caniuse.com/)



## HTML

> **Hyper Text** Markup Language
>
> : 웹 페이지를 작성(구조화)하기 위한 언어

🧷 **Hyper Text** : 참조(하이퍼링크)를 통해 사용자가 한 문서에서 다른 문서로 즉시 접근할 수 있는 텍스트

🧷 **Markup Language** : 태그 등을 이용하여 문서나 데이터의 구조를 명시하는 언어 ==> HTML, Markdown

`.html` : HTML 파일



### HTML 기본 구조

```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Hello, HTML</title>
</head>
<body>
</body>
</html>
```

- html : 문서의 최상위(root) 요소

- head : 문서 메타데이터 요소

  - 문서 제목, 인코딩, 스타일, 외부 파일 로딩 등
  - 일반적으로 브라우저에 나타나지 않는 내용

- body : 문서 본문 요소

  - 실제 화면 구성과 관련된 내용

    

  ![](https://github.com/forwardyoung/TIL/blob/master/WEB/Web_Intro.assets/HTML%201.png)

📍 **head 예시**

```html
	<head>
        <title>HTML 수업</title>
        <meta charset="UTF-8"
        <link href="style.css" rel="stylesheet">
        <script src="javascript.js"></script>
        <style>
          p {
            color: black;
          }
        </style>
    </head>
```

`<title>` : 브라우저 상단 타이틀

`<meta>` : 문서 레벨 메타데이터 요소

`<link>` : 외부 리소스 연결 요소 (CSS 파일, favicon 등)

`<script>` : 스크립트 요소 (JavaScript 파일/코드)

`<style>` : CSS 직접 작성



🌍 **Open Graph Protocol**

- 메타 데이터를 표현하는 새로운 규약
  - HTML 문서의 메타 데이터를 통해 문서의 정보를 전달
  - 메타정보에 해당하는 제목, 설명 등을 쓸 수 있도록 정의

[🔎 참고](https://ogp.me/)



📍 **요소(element)**

![](https://github.com/forwardyoung/TIL/blob/master/WEB/Web_Intro.assets/%EC%9A%94%EC%86%8C.png)

`HTML의 요소는 태그와 내용(contents)로 구성되어 있다.`

- 내용이 없는 태그들도 존재(닫는 태그가 없음)
  - br (띄어 쓰기), hr (수평선), img (이미지), input, link, meta
- 요소는 중첩(nested)될 수 있음 (tab으로 표현)
  - 여는 태그 - 닫는 태그 쌍을 잘 확인할 것!

📍 **속성(attribute)**

![](https://github.com/forwardyoung/TIL/blob/master/WEB/Web_Intro.assets/%EC%86%8D%EC%84%B1.png)

`태그별로 사용할 수 있는 속성은 다르다.`

- 요소는 속성을 가질 수 있으며, 경로나 크기와 같은 추가적인 정보를 제공
- 요소의 시작 태그에 작성하며 보통 이름과 값이 하나의 쌍으로 존재
- 태그와 상관없이 사용 가능한 속성(**HTML Global Attribute**)들도 있음

> 속성 작성 방식 통일하기 ➡️ ""(쌍따옴표) 사용, 공백 X



🧷 **HTML Global Attribute**

`id` : 문서 전체에서 유일한 교유 식별자 지정

`class` : 공백으로 구분된 해당 요소의 클래스의 목록 (CSS, JS에서 요소를 선택하거나 접근)

`style` : inline 스타일

🧷 **[렌더링(Rendering)](https://d2.naver.com/helloworld/59361)**

 : 웹사이트 코드를 사용자가 보게 되는 웹 사이트로 바꾸는 과정

🧷 **DOM(Document Object Model) 트리**

: 텍스트 파일인 HTML 문서를 브라우저에서 렌더링 하기 위한 구조

![문서 객체 모델 - 위키백과, 우리 모두의 백과사전](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/DOM-model.svg/1200px-DOM-model.svg.png)

`<h1>의 부모 태그는 <body>`

`<h1>와 <a>는 형제 관계`



📍 **인라인/블록 요소**

- 인라인 요소 : 글자처럼 취급

- 블록 요소 : 한 줄 모두 사용

  

🔤 **텍스트 요소**

![](https://github.com/forwardyoung/TIL/blob/master/WEB/Web_Intro.assets/%ED%85%8D%EC%8A%A4%ED%8A%B8%20%EC%9A%94%EC%86%8C.png)

`&nbsp;` : 띄어쓰기

`<br>` : 줄바꿈

➡️ 태그간의 띄어쓰기, 엔터는 동작 X

`<!-- 주석 -->`

![](https://github.com/forwardyoung/TIL/blob/master/WEB/Web_Intro.assets/%EC%98%88%EC%8B%9C.png)

🔠 **그룹 컨텐츠**

![](https://github.com/forwardyoung/TIL/blob/master/WEB/Web_Intro.assets/%EA%B7%B8%EB%A3%B9%20%EC%BB%A8%ED%85%90%EC%B8%A0.png)

🍯 **[HTML 태그</> 더 알아보기](https://inpa.tistory.com/entry/HTML-%F0%9F%8F%B7%EF%B8%8F-%ED%83%9C%EA%B7%B8-%EC%9A%94%EC%95%BD%ED%91%9C?category=890791)**



## CSS

> **Cascading Style Sheets**
>
> : 스타일을 지정하기 위한 언어 ➡️ 선택하고 스타일을 지정

![](https://github.com/forwardyoung/TIL/blob/master/WEB/Web_Intro.assets/CSS.png)

- CSS 구문은 선택자를 통해 스타일을 지정할 HTML 요소를 **선택**
- 중괄호 안에서는 속성과 값, 하나의 쌍으로 이루어진 선언을 진행
- 각 쌍은 선택한 요소의 속성, 속성에 부여할 값을 의미
  - **속성 (Property)** : 어떤 스타일 기능을 변경할 지 결정
  - **값 (Value)** : 어떻게 스타일 기능을 변경할 지 결정

📍 CSS 정의 방법 - 내부 참조(embedding)

```html
<head>
        <title>제목</title>
        <style>
            h1{
                color: coral;
                font-size: 15px;
            }
        </style>
    </head>
```

`<head> 태그 내에 <style>에 지정`

📍 CSS 정의 방법 - 외부 참조(link file)

`외부 CSS 파일을 <head>내 <link>를 통해 불러오기`



### CSS with 개발자 도구

- styles : 해당 요소에 선언된 모든 CSS

![](https://github.com/forwardyoung/TIL/blob/master/WEB/Web_Intro.assets/styles.png)

- computed : 해당 요소에 최종 계산된 CSS

![](https://github.com/forwardyoung/TIL/blob/master/WEB/Web_Intro.assets/computed.png)

---

> 💻 CSS는 **선택**해서 스타일을 적용한다.

- 적용에는 **우선순위**가 있다. 

- 같은 레벨이라면 나중에 **'선언'**된 것이 적용된다.

- id, class, 태그는 서로 다른 레벨이다.

- `id(# 문자로 시작) > class(.마침표로 시작) > 태그` 순으로 우선순위를 가진다.

⚠️ 다만, 일반적으로 CSS 스타일링은 클래스로만!

- id는 잘 활용하지 않고, JS로 개발할 때 보통 활용한다.

- id는 문서에서 반드시 **한번만** 등장해야 한다.