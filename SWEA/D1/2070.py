import sys
sys.stdin = open("input_2070.txt", "r")

T = int(input())

for i in range(1, T + 1):
    a, b = list(map(int, input().split()))
    if a < b:
        result ='<'
    elif a == b:
        result = '='
    else:
        result = '>'
    print('#{} {}'.format(i, result))