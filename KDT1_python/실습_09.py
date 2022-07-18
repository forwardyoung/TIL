# 주어진 리스트가 반장 선거 투표 결과일 때 이영희의 총 득표수를 출력
students = ['이영희', '김철수', '이영희', '조민지', '김철수', '조민지', '이영희', '이영희']

number_vote = 0

for i in students:
    if i == '이영희':
        number_vote += 1
print(number_vote)