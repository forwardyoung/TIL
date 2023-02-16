# TCP와 UDP

OSI 7 계층 중 Layer 4 - **전송 계층** 프로토콜에 해당한다.

## TCP(Transmission Control Protocol)

>  신뢰성 있는 데이터 전송을 지원하는 연결 지향형 프로토콜

- 연결 지향형인 TCP는 3-way handshaking이라는 과정을 통해 연결 후 통신을 시작하는데, 흐름 제어와 혼잡 제어를 지원하며 데이터의 순서를 보장한다.
  - 흐름 제어 : 보내는 측과 받는 측의 데이터 처리속도 차이를 조절해주는 것
  - 혼잡 제어 : 네트워크 내의 패킷 수가 넘치게 증가하지 않도록 방지하는 것
- 신뢰성 있는 데이터 전송
- 패킷 손실, 중복, 순서 바뀜 등이 없도록 보장
- [연결을 설정(3-way handshaking)과 해제(4-way handshaking)](https://bangu4.tistory.com/74)

- 인터넷 프로토콜 스위트(IP)의 핵심 프로토콜 중 하나로, IP와 함께 **TCP/IP** 라는 명칭으로 사용된다.
- **전이중(Full Duplex) 방식**의 양방향 가상회선을 제공하고, 전송 데이터와 응답 데이터를 함께 전송할 수 있다.

![img](https://blog.kakaocdn.net/dn/ltwPF/btqNqZ8eeiC/Om0y6XDdsKkq6CvOEzcXe0/img.png)

- 순서 제어, 오류 제어, 흐름 제어 기능 제공

### 📍TCP 헤더 구조

![TCP Header Details, TCP Header](https://1.bp.blogspot.com/-oE1QQcPLscU/Xz1n9yemnoI/AAAAAAAACfM/iS8OVSArtZsPEQ4s_jozoZox1zceqCnCQCLcBGAsYHQ/w640-h386/tcpheader.jpg)

- 전송 데이터가 뒤따른다.

### TCP 흐름 제어

> 전송 계층에서 데이터 패킷을 전송할 때 수신 한도를 넘는 과잉 패킷의 입력으로 패킷 분실이 일어나지 않도록 패킷의 흐름을 조절하는 기법

**1) Stop and Wait** : 매번 전송한 패킷에 대해 확인 응답을 받아야만 그 다음 패킷을 전송하는 방법

 

![img](https://t1.daumcdn.net/cfile/tistory/263B7D4E5715ECEB32)

- 프레임이 손실되었을 때, 손실된 프레임 1개를 전송하고 수신자의 응답을 기다리는 방식으로 한 번에 프레임 1개만 전송할 수 있음

**2) Sliding Window** : 수신측에서 설정한 윈도우 크기만큼 송신측에서 확인 응답(ACK)없이 세그먼트를 전송할 수 있게 하여 데이터 흐름을 동적으로 조절하는 제어기법

![img](https://t1.daumcdn.net/cfile/tistory/253F7E485715ED5F27)

- 호스트는 각 연결마다 하나의 window 이용

  

## UDP(User Datagram Protocol)

> 비연결형 프로토콜로써, 인터넷상에서 서로 정보를 주고받을 때 정보를 보낸다는 신호나 받는다는 신호 절차를 거치지 않고 보내는 쪽에서 일방적으로 데이터를 전달하는 통신 프로토콜



### 📍UDP 헤더 구조

![UDP header format](https://cdn.ttgtmedia.com/rms/onlineimages/networking-udp_mobile.png)

- 경량의 헤더 구조로 데이터그램의 신뢰를 보장하지 않음

## TCP와 UDP 비교

| **TCP(Transfer Control Protocol)**               | **UDP(User Datagram Protocol)**                             |
| ------------------------------------------------ | ----------------------------------------------------------- |
| **연결형 프로토콜**                              | **비연결형 프로토콜**                                       |
| **데이터의 경계를 구분하지 않음**                | **데이터의 경계를 구분함**                                  |
| **신뢰성있는 데이터 전송 (데이터 재전송 존재O)** | **비신뢰성 데이터 전송 (데이터 재전송 존재X)**              |
| **일 대 일(Unicast) 통신**                       | **일 대 일, 일 대 다(Broadcast), 다 대 다(Multicast) 통신** |

![img](https://blog.kakaocdn.net/dn/0E71C/btrlA7FPUnj/sC9ZwQKWS6G5st0KtJwrK0/img.png)