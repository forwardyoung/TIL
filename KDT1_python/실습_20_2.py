# 정수 number가 주어질 때, 각 자릿수의 합을 구해서 출력하세요.
# 접근 방법 : 10으로 나눈 나머지를 더하기!
number = int(input())

result = 0
while number:
    number, remainder = divmod(number, 10)
    result += remainder
print(result)
# divmod(x, y)는 x를 y로 나누고,
# 결과를 tuple로 반환
# (몫, 나머지)