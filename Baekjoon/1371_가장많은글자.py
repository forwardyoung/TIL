import sys

sentence = sys.stdin.read() # 50개의 문장 한 번에 입력받는다.
a_z = [0] * 26 # a부터 z까지 알파벳의 개수 : 26개

for s in sentence: # 문장 sentence에서 s가 순회할 때 
    if s.islower(): # islower() 소문자만 탐색
        a_z[ord(s) - ord('a')] += 1 # s를 숫자로 바꾼 것에서 a의 숫자형을 빼서 해당하는 a_z에 1을 더한다.

for i in range(26):
    if a_z[i] == max(a_z):
        print(chr(i + ord('a')), end='')