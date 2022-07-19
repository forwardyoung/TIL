# 정수 number가 주어질 때, 각 자릿수의 합을 구해서 출력하세요.
# 접근 방법 : 10으로 나눈 나머지를 더하기!
number = int(input())

# number가 0일 때 Stop!
# => int는 0일 때 False
result = 0
while number:
    # 몫은 다음 number가 됨
    # 나머지는 더해나가면 됨
    result += number%10
    number //= 10
print(result)