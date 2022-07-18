# 문자열 word가 주어질 때, 해당 문자열에서 `a` 의 모든 위치(index)를 출력해주세요.
# `find()` `index()` 메서드 사용 금지
word = input()

for i in range(len(word)):
    if word[i] == 'a':
        print(i, end=' ')
        # sep은 출력문들 사이에 내용을 넣는 것이고 end는 출력이 완료된 뒤의 내용을 넣는 것
        # end 개행, end=' ' 띄어쓰기