# 주어진 문자열 word가 주어질 때, 해당 단어에서 ‘a’를 모두 제거한 결과를 출력하시오.

word = 'apple'
result =''
# 반복! for
for char in 'apple':
    # 만약 a 가 아닐 때
    if char != 'a':
        result = result + char
        # 반복문에서 아무것도 안하고 넘어가는?
        # continue!
print(result)