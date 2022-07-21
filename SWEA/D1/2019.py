import sys
sys.stdin = open("input_2019.txt", "r")

n = int(input())

for i in range(n+1):
    print(2**i, end=' ')
    # i는 0부터 8까지.
    # 2의 0제곱은 1!!!

    