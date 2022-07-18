# 아래 코드는 숫자의 길이를 구하는 코드입니다.
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.
# 오류 코드 : number = 22020718
# TypeError: object of type 'int' has no len()
# 원인 : int는 len() 함수를 갖고 있지 않음. 따라서, int에서 str으로 형 변환을 해 준다.
number = 22020718
print(len(str(number)))