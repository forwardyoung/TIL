import sys
sys.stdin = open("input_2049.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    a, b = map(int, input().split())
    x, y = divmod(a, b)
    print(f'#{test_case} {x} {y}')