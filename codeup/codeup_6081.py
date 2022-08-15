n = int(input(), 16) # 16진수로 한 자리 수가 입력 / n = int(input(), 2) ==> 2진수로 입력
for i in range(1, 16):
    print('%X'%n,'*%X'%i, '=%X'%(i*n), sep='') # n*i =곱한 값의 형태로 출력