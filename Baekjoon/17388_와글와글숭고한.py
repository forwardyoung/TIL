import sys
sys.stdin = open("17388.txt")

s, k, h = map(int, input().split())
if s + k + h >= 100:
    print('OK')
else:
    if min(s, k, h) == s:
        print('Soongsil')
    elif min(s, k, h) == k:
        print('Korea')
    elif min(s, k, h) == h:
        print('Hanyang')