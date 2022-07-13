# 주어진 문자열 word가 주어질 때, 해당 단어를 역순으로 뒤집은 결과를 출력하시오.
word = 'apple'
# 1. for
# result = ''
# 비어 있는 문자열을 만들고
# for char in word:
#       result = char + result
    # 거꾸로 더하기
# print(result)

# 2. pythonic
# print(word[::-1])
# print(''.join(reversed(word)))

# 3. index
# 익숙해질수록 나중에 알고리즘 코드 풀기 좋음
word = 'apple'

for i in range(len(word)):
    print(word[len(word)-i-1], end='')
# 0 1 2 3 4 를 4 3 2 1 0으로
