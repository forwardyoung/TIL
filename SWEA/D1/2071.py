import sys
sys.stdin = open("input_2071.txt", "r")

T = int(input())

for i in range(1, T + 1):
    n = list(map(int, input().split()))
    avg = sum(n) / len(n)

    print('#{} {}'.format(i, round(avg)))
    # round : avg 값이 28.6이 나올 때 29로 출력하기 위해 반올림 해준다.