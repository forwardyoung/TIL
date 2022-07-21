import sys
sys.stdin = open("input_2050.txt", "r")
t = input()
l = list(t)
result = ''.join(map(str, l))
for i in result:
    b= ord(i)-64
    print(b, end=' ')