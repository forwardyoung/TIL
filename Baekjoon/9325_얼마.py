import sys
input = sys.stdin.readline
T = int(input())
for tc in range(1, T+1):
    total = 0
    cost = int(input()) # 자동차의 가격
    n = int(input()) # 옵션의 개수
    for _ in range(n):
        q, p = map(int, input().split())
        total += (q * p)
    print(total + cost)