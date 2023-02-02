# 네트워크 7계층 (OSI 7 Layer)



## OSI(Open System Interconnection) 7계층

> 국제 표준화 기구인 ISO(International Standardization Organization)에서 개발한 컴퓨터 네트워크 프로토콜 디자인과 통신을 계층으로 나누어 설명한 개방형 시스템 상호 연결 모델

**❔ OSI 7단계로 정의한 이유** : 통신이 일어나는 과정을 *단계별로 파악*하기 위함과 통신 과정 중에서 특정한 곳에 이상이 생길 경우에 다른 단계의 장비 및 소프트웨어 등을 건드리지 않고 통신 장애를 일으킨 단계에서 해결할 수 있기 때문 

**➡️ 각 계층은 서로 독립적으로 구성됨**



![파일:OSI 7 계층.jpg](http://wiki.hash.kr/images/7/71/OSI_7_%EA%B3%84%EC%B8%B5.jpg)

- 계층을 지날 때마다 **헤더(Header)**가 붙는데, 이것은 해당 계층의 기능과 관련된 제어 정보가 포함되어 있다.

| 계층 이름                         | 첫 알파벳 | /          |
| --------------------------------- | --------- | ---------- |
| 응용 계층 (Application Layer)     | A         | 앞         |
| 표현 계층 (Presentation Layer)    | P         | 페         |
| 세션 계층 (Session Layer)         | S         | 서         |
| 전송 계층 (Transport Layer)       | T         | 터지       |
| 네트워크 계층 (Network Layer)     | N         | 니         |
| 데이터링크 계층 (Data-Link Layer) | D         | 뒤에서     |
| 물리 계층 (Physical Layer)        | P         | 피가나더라 |



## 작동 원리

- 전송 시 7계층에서 1계층으로 각각의 층마다 인식할 수 있어야 하는 헤더를 붙임(캡슐화)
- 수신 시 1계층에서 7계층으로 헤더를 떼어냄(디캡슐화)



**참고**

- [네트워크 OSI 7Layer / 7계층 개념 및 역할, 구조까지 한번에 알아보기](https://onecoin-life.com/19)
- [OSI 7 계층](http://wiki.hash.kr/index.php/OSI_7_%EA%B3%84%EC%B8%B5)
- [[네트워크] OSI 7 계층 (OSI 7 LAYER) 기본 개념, 각 계층 설명](https://velog.io/@cgotjh/%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC-OSI-7-%EA%B3%84%EC%B8%B5-OSI-7-LAYER-%EA%B8%B0%EB%B3%B8-%EA%B0%9C%EB%85%90-%EA%B0%81-%EA%B3%84%EC%B8%B5-%EC%84%A4%EB%AA%85)