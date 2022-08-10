# word = input().split() ==> split()으로 입력받으면 이모티콘 바로 뒤에 다른 문자가 입력될 때 이모티콘의 개수를 제대로 세지 못함!
# print(word) ==> ['How', 'are', 'you', ':-)', 'doing', ':-(', 'today', ':-)?']

word = input()
smile = ':-)'
crying = ':-('

if word.count(smile) > word.count(crying):
    print('happy')
elif word.count(smile) < word.count(crying):
    print('sad')
elif word.count(smile) == 0 and word.count(crying) == 0: # 조건문 순서에 따라 none이 출력될 수도 있고
    print('none')
elif word.count(smile) == word.count(crying): # unsure만 출력될 수도 있음
    print('unsure')