c = input()
# print(ord(c)) --> 입력한 알파벳의 정수값 출력
t = ord('a')
# print(ord('a')) --> 소문자 a의 정수값 : 97
while t <= ord(c): # t값이 c의 정수값과 같아질 때까지
    print(t, end=' ') # t를 출력하고
    t += 1 # t에 1씩 더해 while 반복문 순회