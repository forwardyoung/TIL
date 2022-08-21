a, b, c = map(int, input().split())
day = 1 # 1일부터 차례로 증가시킬 것
while True:
    # day에 저장된 현재 날짜에 인원이 모두 방문한 날이라면,
    # 즉, day의 값을 각 인원의 방문 주기로 나누었을 때 나머지가 모두 0이라면
    if day % a == 0 and day % b == 0 and day % c == 0:
        # 3명이 다시 함께 방문하는 날이므로 day를 출력하낟.
        print(day)
        break

    day += 1 # 3명이 다시 함께 방문하는 날이 아니면 그 다음 날을 생각해야 하므로 day에 1을 더한다.