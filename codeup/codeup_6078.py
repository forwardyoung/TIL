# 무한루프에 빠질 수 있으므로 while문과 input의 순서를 잘 따져보자.
while True:
    word = input()
    print(word)
    if word == 'q':
        break # q가 입력되면 즉시 종료