# > 양의 정수 number가 주어질 때, 숫자의 길이를 구하시오. 
# 양의 정수 number를 문자열로 변경하는 것은 금지입니다. str() 사용 금지 -- print(len(str(number)))
number = 123
# 123 == 100 + 20 + 3 -- 1**100 + 2*10 + 3*1
# number를 10으로 계속 나누다가 몫이 0일 때'까지' 실행 - while의 종료 조건 : 몫이 0
cnt = 0
while number:
# while number != 0으로 써도 무방
    # != 0 같지 않다
    # int : 0이 아닌 다른 수면 무조건 True, 0이 되면 False
    # result = result // 10
    number //= 10
    cnt += 1

print(cnt)

# 3. log
import math
number = 123456
print(int(math.log(number, 10)) + 1) # 상용대수 log 123456을 하면 5가 나오므로 1을 더해줘야 함.
