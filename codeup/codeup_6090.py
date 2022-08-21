a, m, d, n = map(int, input().split())

for i in range(1, n):
    a = a*m + d # 초기값 a를 갱신한다.
print(a)