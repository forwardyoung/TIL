# 아래 코드는 문자열을 입력받아 단어별로 나누는 코드입니다.
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.
# 오류 코드
# words = list(map(int, input().split()))
# 원인 : I'm Tutor라는 값이 int()에 적절하지 않음
# words = list(input().split(), map(int, input().split())) 
# 위 코드 에러 : TypeError : list expected at most 1 argument, got 2 argument - argument 개수 초과
words = list(input().split())
print(words)
