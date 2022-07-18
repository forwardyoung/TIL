# 아래 코드는 문자열에서 모음의 개수를 찾는 코드입니다. 
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.
word = "HappyHacking"

count = 0

for char in word:
    # 오류 if char == "a" or "e" or "i" or "o" or "u":
    # if char == "a"가 or "e"보다 먼저 연산된다. 따라서 char 각각을 모음과 매칭해야 한다. 
    if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
        count += 1

print(count)