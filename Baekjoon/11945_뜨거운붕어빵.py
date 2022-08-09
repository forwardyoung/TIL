import sys
input = sys.stdin.readline

n, m = map(int, input().split())
for _ in range(n):
    list = input() # 0과 1의 모음
    print(list[::-1])