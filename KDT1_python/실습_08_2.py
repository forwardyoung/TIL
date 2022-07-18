# 주어진 리스트 numbers에서 두번째로 큰 수를 구하기
# max() 함수 사용 금지
# 두 번째로 큰 수를 기록
numbers = [-10, -100, -30]
max_number = numbers[0]
second_number = numbers[0]
# 1. 전체 숫자를 반복
for n in numbers:
    # 만약에, n이 최대보다 크다면
    if max_number < n:
        #최대값이었던 것이 두번째로 큰 수
        second_number = max_number
        max_number = n
    # elif second_number < n < max_number:
    elif second_number < n and n < max_number:
        second_number = n
print(second_number)