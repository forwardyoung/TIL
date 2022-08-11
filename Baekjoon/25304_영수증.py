import sys
sys.stdin = open("25304.txt")

x = int(input()) # 영수증에 적힌 총 금액
n = int(input()) # 물건의 종류의 수 
whole_price = [] # 계산한 금액 합

for _ in range(n):
    a, b = map(int, input().split())
    whole_price.append(a*b)
if sum(whole_price) == x:
    print('Yes')
else:
    print('No')