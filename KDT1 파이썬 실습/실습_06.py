# 리스트에서 최댓값 구하기
numbers = [0, 20, 100]
max = numbers[0] # 임의로 가장 앞의 값을 max 변수에 넣어두고 리스트가 돌아가면서 하나씩 비교!

for num in numbers:
    if max < num:
        # 만약, max 값이 num보다 작으면 바꾼다.
        max = num
print(max)
