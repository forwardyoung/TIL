import sys
sys.stdin = open("input_1986.txt", "r")
# 풀이 1
T = int(input())

for i in range(1, T + 1):
    n = int(input())
    result = 0
    for N in range(1, n+1):
        if N % 2 == 1:
            result = result +N 
        elif N % 2 == 0:
            result = result -N
    print('#{} {}'.format(i, result))

# 풀이 2
# T = int(input())

# for i in range(1, T + 1):
#     n = int(input())
#     if n % 2 == 1:
#         print('#{} {}'.format(i, int((n+1)/2))) -- 소수점까지 출력되므로 정수형 int!
#     else:
#         print('#{} {}'.format(i, int(-n/2)))