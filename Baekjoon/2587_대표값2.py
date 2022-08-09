import sys
input = sys.stdin.readline

numbers = []
for _ in range(5):
    numbers.append(int(input()))
    numbers.sort()
# print(numbers) ==> [10, 30, 30, 40, 60]
print(sum(numbers) // 5) # 평균값 자연수로 출력 '//' 사용
print(numbers[2])
