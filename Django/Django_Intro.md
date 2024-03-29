## HTTP

웹 사이트 동작 방식
➡️ 웹 브라우저 주소창에 URL 입력 후 엔터
➡️ URL을 이용해서 서버의 IP를 찾는다.
➡️ IP를 이용해서 서버에 접속
➡️ URL에 해당하는 자료를 요청
➡️ 웹 어플리케이션이 URL을 해석해서 해당하는 코드가 동작
➡️ 코드의 동작 결과를 응답으로 돌려줌
➡️ 서버가 -> 웹 브라우저로 데이터를 보내줌
➡️ 웹 브라우저 응답받은 데이터를 화면에 표시
➡️ * JS(AJAX)

백엔드 코드 : 각각의 URL 패턴마다 소스코드 1개 이상 ex) 일반 면요리

> Framework : 어떤 일을 할 때 자주 사용되는 기능을 미리 준비해둔 것.
> ➡️ 제품을 빨리 출시하기 위해 등장
>  ex) 라면을 끓이는 것

- Micro : 최소한의 기능만 가지고 있다 + 추가 기능을 원하는 대로 설치해서 사용 customizing하기 쉬움(Flask)

- Fullstack : 거의 대부분의 기능을 가지고 있다 + 추가 기능도 설치 가능 (Django)

  

> 디자인 패턴 : 개발 설계상 발생하는 문제를 해결하기 위한 해결책 (디자이너, 프론트, 백엔드)

- MVC : Model(DB), View(화면-프론트), Controller(계산, 처리 - 백엔드)

- MTV : Model(DB), Template(화면-프론트), View(계산, 처리 - 백엔드)

  

## 장고로 프로젝트 만드는 순서

1. 프로젝트 만들기
2. 장고 설치
3. 장고 프로젝트 만들기
4. 설정하기 (DB, S3)
5. DB 초기화
6. 관리자 계정 만들기 <br> 

7. 앱 만들기 (기능별)
8. 모델 설계 (DB)

9. 뷰 만들기 (기능, 계산) <br> 
10. 템플릿 만들기 (화면에 표시될 내용, 양식 HTML)
11. URL을 만든다.
대표적인 기능(화면) : CRUD -> Create(회원가입), READ(회원정보 조회), Update(수정), Delete(탈퇴)

