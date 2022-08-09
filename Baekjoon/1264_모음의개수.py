collection = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
while True:
    sentence = input()
    cnt = 0
    if sentence == '#':
        break
    for i in sentence:
        if i in collection:
            cnt += 1
    print(cnt)
