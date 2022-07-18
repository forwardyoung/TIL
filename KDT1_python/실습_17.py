# 소문자로 구성된 문자열 word가 주어질 때, 모두 대문자로 바꾸어 표현하시오.
# .upper(), .swapcase() 사용 금지
# 대소문자 Chr 값 차이 : 32 --- 
# 1) 소문자 숫자형 - 32 = 대문자 숫자형 
# 2) 대문자 숫자형을 알파벳으로
word = 'banana'
result = ''
for char in word:
    # print(ord(char)) -- 98 97 110 97 110 97
    number = ord(char)
    number = number-32
    result += chr(number)
print(result)

# 다음과 같이 줄일 수 있음.
for char in word:
    print(chr(ord(char)-32))