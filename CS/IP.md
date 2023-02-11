# 📃 IP

> Internet Protocol : 송신 호스트와 수신 호스트가 패킷 교환 네트워크에서 정보를 주고받는 데 사용하는 정보 위주의 규약

**패킷** : pack + bucket, 컴퓨터 간에 데이터를 주고받을 때 네트워크를 통해서 전송되는 데이터 조각

- OSI 3계층인 네트워크 계층에서 호스트의 주소 지정과 패킷 분할 및 조립 기능을 담당

  ![img](https://blog.kakaocdn.net/dn/bahNj1/btrybWZ0zzg/LcTh7dMleYzRaIejcsqzk0/img.png)

  - 편지를 보낼 때 주소를 적듯이, 전송 데이터 이외에 출발지 IP와 목적지 IP가 필요

- IP의 정보는 패킷 혹은 데이터그램이라고 하는 덩어리로 나뉘어 전송

  ![img](https://blog.kakaocdn.net/dn/5JPdT/btryf0skr2F/FhwXP6a78Yl0orG8e9SOVK/img.png)

  - IP 패킷을 만들어서 인터넷망에 던지면, 프로토콜에 따라서 최종적으로 목적지 IP가 할당된 서버까지 전달됨



## IP의 특징

1) 비신뢰성(Unreliable) : 중간에 패킷이 사라져도 IP 프로토콜에서 전송하는 데이터가 정확하게 갔는지 확인하지 않는다. (패킷 전달 여부에 대해서 보증하지 않는다).

2. 비연결성(Connectionless) : 패킷을 받을 대상이 없거나 서비스 불능 상태여도 패킷을 전송함 (ex) 컴퓨터가 꺼진 경우) 

3. 프로그램 구분 불가능 : 한 PC에서 여러개의 애플리케이션 (EX) 게임, Youtube)들이 같은 IP를 쓰는 상황에서 전송받은 패킷이 어떤 애플리케이션에 해당하는지 알 수 없음
4. IP 크기 제한 
   - IP의 크기는 20~40 바이트
   - IP 패킷은 네트워크가 수용할 수 있는 크기로 분활되어야 하는데, 이를 단편화(Fragmentation)라 함
   - 인터넷으로 데이터를 전송 시에는 IP 패킷을 잘라서 보내고, 이런 단편화는 **MTU(인터넷에서 최대로 보낼 수 있는 메시지 단위)** 때문에 필요함. 



**참고**

- [[HTTP] 인터넷 프로토콜(IP)의 특징과 한계](https://wschoi.tistory.com/33)
