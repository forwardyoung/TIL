a, b = input().split()
a, b = int(a), int(b)
answer = bool(a) and bool(b) # a와 b 모두 0이 아닌 정수이므로 True
print(answer) # boolean AND의 출력값 : True