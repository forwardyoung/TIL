w, h, b = map(int, input().split())
result = w*h*b/8/1024/1024
# %.nf앞의 숫자(n)만큼 소수점 이하 출력 = 그 이후 자리에서 반올림
print("%.2f MB" % (result))