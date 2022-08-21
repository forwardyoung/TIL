n = int(input())
number = list(map(int, input().split()))
result = list(0 for _ in range(24)) # [0, 0, 0, ''']

for i in range(n):
    result[number[i]] += 1 # #번호를 부를 때마다, 그 번호에 대한 카운트 1씩 증가

for i in range(1, 24): # 1~23까지
    print(result[i], end = " ")