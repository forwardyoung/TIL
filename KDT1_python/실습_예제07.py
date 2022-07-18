# 아래 코드는 평균을 구하는 논리적으로 오류가 있는 코드입니다. 
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

total = 0
count = 0

# for number in number_list:
#    total += number
# count += 1
# 오류 원인 : count의 위치가 for 조건문과 무관하므로 print(count) 하면 출력값이 1이 나와서 55를 1로 나누게 됨.

for number in number_list:
    total += number
    count += 1
# 이때 print(total//count)를 하면 int형의 5가 출력된다. 따라서 5.5라는 출력값이 나오려면 total/count로!
print(total/count)
