import sys
input = sys.stdin.readline
N = int(input())
seat = list(map(int, input().split())) # 손님이 안고 싶어하는 자리의 번호
number = [0 for _ in range(101)] # 자리 1~100까지 있고, 배열의 index는 0부터 시작이므로 101개 배열의 크기
cnt = 0 # 거절당한 사람 수
for i in seat:
    if number[i] == 0: # 자리의 값이 0이면 -- 앉은 사람이 없으면
        number[i] = 1 # 1을 할당한다.
    else:
        cnt += 1 # 그렇지 않으면 거절당한 사람 수에 1을 더한다.
print(cnt)