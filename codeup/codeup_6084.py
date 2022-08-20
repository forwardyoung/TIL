h, b, c, s = map(int, input().split())
result = round(h*b*c*s/8/1024/1024, 1) # round(n, 2) => n을 반올림하여 소수점 두번째 자리까지
print(result, "MB")
