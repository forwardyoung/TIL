## JavaScript Intro

**🌍 브라우저(browser)**

: `URL로 웹(WWW)을 탐색하며 서버와 통신하고, HTML 문서나 파일을 출력하는 GUI 기반의 소프트웨어`

- 인터넷의 컨텐츠를 검색 및 열람하도록 함

- "웹 브라우저"라고도 함

- 주요 브라우저 : `Google Chrome, Mozilla Firefox, Microsoft Edge, Opera, Safari`

  

**JavaScript의 필요성**

- 브라우저 화면을 '동적'으로 만들기 위함

- `브라우저를 조작할 수 있는 유일한 언어`

![html css javascript](https://html-css-js.com/images/og.jpg)



## History of JavaScript

🔎 **[참고](https://poiemaweb.com/js-introduction)**

`JavaScript의 탄생 ➡️ 제1차 브라우저 전쟁 ➡️ 제2차 브라우저 전쟁 ➡️ 파편화와 표준화`

🌍 **제2차 브라우저 전쟁**

- MS vs Google
- 2008년 Google의 Chrome 브라우저 발표
- 2011년 3년 만에 파이어폭스의 점유율을 돌파 후 2012년부터 전세계 점유율 1위
- 크롬의 승리 요인
  - 압도적인 속도
  - 강력한 개발자 도구 제공
  - 웹 표준

🌍 **파편화와 표준화**

- 제1차 브라우저 전쟁 이후 수많은 브라우저에서 자체 자바스크립트 언어를 사용하게 됨
- 결국 서로 다른 자바스크립트가 만들어지면서 크로스 브라우징 이슈가 발생하여 웹 표준의 필요성이 제기
- 크로스 브라우징
  - W3C에서 채택된 표준 웹 기술을 채용하여 각각의 브라우저마다 다르게 구현되는 기술을 비슷하게 만들되, 어느 한쪽에 치우치지 않도록 웹 페이지를 제작하는 방법론 (동일성이 아닌 동등성)
  - 브라우저마다 렌더링에 사용하는 엔진이 다르기 때문

- 1996년 11월, 넷스케이프는 컴퓨터 시스템의 표준을 관리하는 비영리 표준화 기구인 [ECMA 인터내셔널](https://www.ecma-international.org/)에 자바스크립트의 표준화를 요청

- 1997년 ECMAScript 1 (ES1) 탄생
- 언어의 파편화를 해결하기 위해 각 브라우저 회사와 재단은 표준화에 더욱 적극적으로 힘을 모으기 시작

🌍 **JavaScript ES6+**

![ecmascript versions - evolution](https://www.pentalog.com/wp-content/uploads/2020/02/ecmascript-versions-evolution.jpg)

- 2015년 ES2015 (ES6) 탄생
- JavaScript의 고질적인 문제들을 해결하고 JavaScript의 다음 시대라고 불릴 정도로 많은 혁신과 변화를 맞이한 버전
- 이때부터 버전 순서가 아닌 출시 연도를 붙이는 것이 공식 명칭이나 통상적으로 ES6라 부름

- 현재는 표준 대부분이 ES6+로 넘어옴

🌍 **Vanilla JavaScript**

- 크로스 브라우징, 간편한 활용 등을 위해 많은 라이브러리 등장 (jQuery 등)
- ES6 이후, 다양한 도구의 등장으로 순수 자바스크립트 활용의 증대

> ❓ **Node.js**
>
> : 자바스크립트에 Runtime 환경을 제공해주는 도구 ➡️ `자바스크립트 실행 환경`

**Node.js** 의 등장으로 자바스크립트는 웹 브라우저를 벗어나 서버 사이드 애플리케이션 개발에서도 사용되는 범용 프로그래밍 언어가 되었다.

🔎 **[참고](https://hanamon.kr/nodejs-%EA%B0%9C%EB%85%90-%EC%9D%B4%ED%95%B4%ED%95%98%EA%B8%B0/)**



## DOM(Document Object Model)

**브라우저에서 할 수 있는 일**

✔️ DOM 조작

- 문서(HTML) 조작

✔️ BOM 조작

- navigator, screen, location, frames, history, XHR

✔️ JavaScript Core (ECMAScript) : 프로그래밍 문법

- Data Structure(Object, Array), Conditional Expression, Iteration

### 💻 DOM

- HTML, XML과 같은 문서를 다루기 위한 **문서 프로그래밍 인터페이스**
- 문서를 **구조화**하고 구조화된 구성 요소를 **하나의 객체로 취급**하여 다루는 논리적 트리 모델

- 문서가 구조화되어 있으며 각 요소는 객체(object)로 취급
- 단순한 속성 접근, 메서드 활용뿐만 아니라 프로그래밍 언어적 특성을 활용한 조작 가능
- 주요 객체
  - `window` : DOM을 표현하는 창. **가장 최상위 객체* (작성 시 생략 가능)
  - `document` : 페이지 컨텐츠의 Entry Point 역할을 하며,  <body> 등과 같은 수많은 다른 요소들을 포함
  - navigator, location, history, screen

![DOM-model.svg](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/DOM-model.svg/800px-DOM-model.svg.png)

### 💻 DOM - 해석

- 파싱(Parsing)
  - 구문 분석, 해석
  - 브라우저가 문자열을 해석하여 DOM Tree로 만드는 과정

![img](https://2r4s9p1yi1fa2jd7j43zph8r-wpengine.netdna-ssl.com/files/2017/08/05-01.png)

![img](https://2r4s9p1yi1fa2jd7j43zph8r-wpengine.netdna-ssl.com/files/2017/08/05-02.png)

![05-3.png (2261×1677)](https://2r4s9p1yi1fa2jd7j43zph8r-wpengine.netdna-ssl.com/files/2017/08/05-3.png)

### 💻 BOM

- Browser Object Model

- 자바스크립트가 브라우저와 소통하기 위한 모델

- 브라우저의 창이나 프레임을 추상화해서 프로그래밍적으로 **제어**할 수 있도록 제공하는 수단

  - 버튼, URL 입력창, 타이틀 바 등 브라우저 윈도우 및 웹 페이지 일부분을 제어 가능

- window 객체는 모든 브라우저로부터 지원받으며 브라우저의 창(window)를 지칭

  

**BOM 조작**

```javascript
// 탭 창
window.open

// 인쇄 창
window.print()

// 메시지 및 확인, 취소 버튼이 있는 대화상자 창
window.confirm()

// document도 브라우저 내에 종속되어 있기 때문에 window 전역 객체에 포함
window.document
```



**JavaScript Core**

- 프로그래밍 언어

```javascript
const numbers = [1, 2, 3, 4, 5]

for (let i=0; i< numbers.length; i++) {
    console.log(numbers[i])
}
```

`브라우저(BOM)과 그 내부의 문서(DOM)를 조작하기 위해 ECMAScript(JS)를 학습`



### 💻 DOM 조작

`Document는 문서 한 장(HTML)에 해당하고 이를 조작`

**DOM 조작 순서**

1. 선택(Select)
2. 변경(Manipulation)



**Document 위치**

![Important parts of web browser; the document is the web page. The window includes the entire document and also the tab. The navigator is the browser, which includes the window (which includes the document) and all other windows.](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Client-side_web_APIs/Manipulating_documents/document-window-navigator.png)

**DOM 객체의 상속 구조**

✔️ **EventTarget** : Event Listener를 가질 수 있는 객체가 구현하는 DOM 인터페이스

✔️ **Node** : 여러 가지 DOM 타입들이 상속하는 인터페이스

✔️ **Element** : Document 안의 모든 객체가 상속하는 가장 범용적인 인터페이스

- 부모인 Node와 그 부모인 EventTarget의 속성을 상속

✔️ **Document** : 브라우저가 불러온 웹 페이지를 나타냄

- DOM 트리의 진입점(entry point) 역할을 수행

✔️ **HTMLElement** : 모든 종류의 HTML 요소

- 부모 element의 속성 상속

---

![image-20220918214237918](C:\Users\726jo\AppData\Roaming\Typora\typora-user-images\image-20220918214237918.png)

자바스크립트에서는 변수를 선언할 때 **키워드가 필요**

- var : 변수를 선언하는 방법이지만, 모던 자바스크립트에서는 더 이상 사용하지 않음
- let : 변수를 생성(선언). 재할당(변경)이 가능하다.
- const : 변화하지 않는 변수(상수)를 선언 할 때에는 const 키워드를 사용

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
  </head>
  <body>
    <!-- JS 코드를 작성하는 영역-->
    <script>
      console.log("hello, js!")
      // h1 요소(element)를 만들고 
      const title = document.createElement('h1')
      // 텍스트를 추가하고
      title.innerText = 'JS 기초'
      // 선택자로 body태그를 가져와서 
      const body = document.querySelector('body')
      // body태그에 자식 요소로 추가(appendChild)
      body.appendChild(title)
    </script>
  </body>
</html>
```

📍 **선택 관련 메서드**

`document.querySelector(selector)` 

- 제공한 선택자와 일치하는 element **하나** 선택

- 제공한 CSS selector를 만족하는 첫 번째 element 객체를 반환 (없다면 null)

`document.querySelectorAll(selector)`

- 제공한 선택자와 일치하는 여러 element(전부)를 선택
- 매칭할 하나 이상의 셀렉터를 포함하는 유효한 CSS selector를 인자(문자열)로 받음

- 지정된 셀렉터에 일치하는 NodeList를 반환

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
  </head>
  <body>
    <h1 id="title">JS 기초</h1>
    <h2>DOM 조작</h2>
    <p class="text">querySelector</p>
    <p class="text">querySelectorAll</p>

    <script>
      // 선택자를 활용해 선택할 때
      // 하나를 선택한다 => querySelector
      // 모든 결과를 선택한다 => querySelectorAll

      console.log(document.querySelector("#title"))
      // <h1 id="title">JS 기초</h1>
      console.lot(document.querySelectorAll(".text"))
      // NodeList(2) [p.text, p.text]
      console.log(document.querySelector(".text"))
      // <p class="text">querySelector</p>
    </script>
  </body>
</html>
```

![image-20220918223054683](C:\Users\726jo\AppData\Roaming\Typora\typora-user-images\image-20220918223054683.png)

⚠️ **return이 무엇인지 아는 게 중요**

`getElementById(id)`

`getElementsByTagName(name)`

`getElementsByClassName(names)`

> ❓`querySelector()`, `querySelectorAll()`을 사용하는 이유
>
> : id, class 그리고 tag 선택자 등을 모두 사용 가능하므로, 더 구체적이고 유연하게 선택 가능
>
> ex) `document.querySelector('#id’)`, `document.querySelectAll(‘.class')`

✔️ 선택 메서드별 반환 타입

- 단일 element : `querySelector()`

- NodeList : `querySelectorAll()`

live collection 안 씀



