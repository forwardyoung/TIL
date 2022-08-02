import sys
input = sys.stdin.readline("25192.txt")

N = int(input())
cnt = 0 # 곰곰티콘 사용한 횟수를 0으로 초기화
user = set() # user라는 set선언

for _ in range(N):
    chat = input() # 채팅 기록 입력 받는다.

    if chat == "ENTER": # 채팅 기록이 ENTER면
        cnt += len(user) # user에 있는 사람의 수를 cnt에 더한다.
        user = set() # set()을 입력하지 않으면 두, 세 '''번째 ENTER 이후에 중복되는 user의 곰곰티콘을 셀 수 없음.
    else:
        user.add(chat) # ENTER가 아니면 chat을 user에 더한다.
cnt += len(user) # user에 있는 사람의 수를 cnt에 더한다.
print(cnt)