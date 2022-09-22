# Django Server

> 🔎 IP와 도메인은 무엇일까요?

> 🔎 HTTP는 무엇이고 요청과 응답 메시지 구성은 어떻게 되나요?

➡️ **HTTP는 HTML 문서와 같은 리소스들을 가져올 수 있도록 해주는 프로토콜**

 HTTP는 웹에서 이루어지는 모든 데이터 교환의 기초이며, **클라이언트-서버 프로토콜**이기도 합니다.

클라이언트-서버 프로토콜이란 (보통 웹브라우저인) 수신자 측에 의해 요청이 초기화되는 프로토콜을 의미합니다.

하나의 완전한 문서는 텍스트, 레이아웃 설명, 이미지, 비디오, 스크립트 등 불러온(fetched) 하위 문서들로 재구성됩니다.

클라이언트와 서버들은 (데이터 스트림과 대조적으로) 개별적인 메시지 교환에 의해 통신합니다.

보통 브라우저인 클라이언트에 의해 전송되는 메시지를 **요청(requests)**이라고 부르며, 그에 대해 서버에서 응답으로 전송되는 메시지를 **응답(responses)**이라고 부릅니다.



📍 **요청의 구성 요소**

- HTTP 메서드, 보통 클라이언트가 수행하고자 하는 동작을 정의한 `GET`, `POST`같은 동사나 `OPTIONS`나 `HEAD`와 같은 명사입니다.

  일반적으로, 클라이언트는 리소스를 가져오거나(`GET`을 사용하여) HTML 폼의 데이터를 전송(`POST`를 사용하여)하려고 하지만,

  다른 경우에는 다른 동작이 요구될 수도 있습니다.

- 가져오려는 리소스의 경로; 예를 들면 프로토콜 (`http://`), 도메인, 또는 TCP 포트인 요소들을 제거한 리소스의 URL입니다.

- HTTP 프로토콜의 버전.

- 서버에 대한 추가 정보를 전달하는 선택적 헤더들.

- `POST`와 같은 몇 가지 메서드를 위한, 전송된 리소스를 포함하는 응답의 본문과 유사한 본문.

📍 **응답의 구성 요소**

- HTTP 프로토콜의 버전.
- 요청의 성공 여부와, 그 이유를 나타내는 상태코드.
- 아무런 영향력이 없는, 상태 코드의 짧은 설명을 나타내는 상태 메시지.
- 요청 헤더와 비슷한, HTTP 헤더들.
- 선택 사항으로, 가져온 리소스가 포함되는 본문.