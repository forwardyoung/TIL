# 리스트에서 최솟값 구하기
numbers = [-10, -100, -30]
min = numbers[0] #0의 의미가 숫자 0이 아닌 list의 첫 번째 값!!!

for num in numbers:
    if min > num:
        min = num
print(min)
