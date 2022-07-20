import sys
sys.stdin = open("input_1933.txt", "r")
# 정수 N 의 모든 약수를 오름차순으로 출력한다.
N = int(input())
for i in range(1, N+1):
    if N % i ==0:
        # 정수 N을 i(1~N까지)로 나눌 때 나머지가 0이면 그 때 i는 약수이다.
        print(i, end=' ')