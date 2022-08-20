n = int(input())
result = 0

for i in range(1, n+1):
    result += i
    if result >= n: # 다 더한 값이 n보다 커지면
        print(result) # 바로 출력
        break