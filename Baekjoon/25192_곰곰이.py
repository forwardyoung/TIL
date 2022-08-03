# 풀이 1
import sys
input = sys.stdin.readline

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

# 풀이 2
N = 7
gom = 0 # 곰곰티콘 사용 횟수
log_list = ["ENTER", "pjshwa", "chansol", "chogahui05", "ENTER", "pjshwa", "chansol"]
set_ = set()
for log in log_list :
    if log == "ENTER": # log가 ENTER라면
        set_.clear() # 기존에 있던 것을 clear로 지워준다.

    else: # log가 ENTER가 아닐 때
    # 닉네임 = log
    # 리스트에서 중복을 탐색할 때는 N만큼의 시간이 필요함.
    # set에서 중복을 탐색할 때는 1만큼의 시간이 필요함!
        if log not in set_: # 닉네임이 set_에 없을 때만 
            set_.add(log) # 새로운 닉네임을 set_에 저장하고
            gom += 1 # 곰곰티콘 횟수 + 1
print(gom)