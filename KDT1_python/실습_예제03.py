# 두 수를 Input으로 받아 합을 구하는 코드이다.
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.
# 오류 코드
# numbers = input().split()
# 원인 : numbers는 str으로 이루어진 list이다. numbers에서 받은 두 수를 더하기 위해서는 int로 형 변환을 해야 한다. 
# map(적용할 함수, 반복 가능한 자료형)
# numbers = int(input().split()) -- int함수 : 리스트는 정수형으로 바꿀 수 없다!
numbers = map(int, input().split())
print(sum(numbers))