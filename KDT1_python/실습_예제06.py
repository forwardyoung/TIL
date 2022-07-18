# 아래 코드는 1부터 N까지의 숫자에 2를 곱해서 변수에 저장하는 코드입니다.
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.
# 오류 코드
# answer = () -- 튜플
# answer.append(number * 2) --- AttributeError: 'tuple' object has no attribute 'append'
# 속성 오류 : 수정이 불가능한 튜플은 append(추가)라는 속성을 갖고 있지 않음.
# Output에 힌트가 있음. 리스트로 선언을 한다.
N = 10
answer = []
for number in range(N + 1):
    answer.append(number * 2)

print(answer)