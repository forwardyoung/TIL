a, r, n = map(int, input().split())
# 등비수열의 일반항 (an) = a 곱하기 r의 n-1 제곱
result = a*r**(n-1)
print(result)