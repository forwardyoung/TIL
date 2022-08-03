import sys
sys.stdin = open("25192.txt")

N = int(input()) 
chat_dict = {} # 사람 이름을 담을 딕셔너리

cnt = 0 # 곰곰티콘 사용 횟수 0으로 초기화
for i in range(N): 
    chat = input().rstrip() # 채팅 기록 입력
    if chat != 'ENTER': # 입력된 게 'ENTER'가 아닌 사람 이름일 때
        if chat not in chat_dict: # 기존에 인사를 안했으면, value를 1로
            chat_dict[chat] = 1
    else: # 'ENTER' 일떄, 입장. 딕셔너리를 초기화 하기전에 value가 1이었던 사람 cnt+1
        for k, v in chat_dict.items():
            if v == 1:
                cnt += 1
        chat_dict = {} # 초기화

for k, v in chat_dict.items(): # 마지막 번째에서, value가 1인 사람들 수 cnt에 +1
    if v == 1:
        cnt += 1
print(cnt) # 총 cnt 출력