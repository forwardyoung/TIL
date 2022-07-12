# 1) while 문
n = 1
result = 1
user_input = int(input())

while n <= user_input:
    result *= n
    n += 1
    
print(result)

# 2) for 문
n = 5
result = 1
for i in range(1,n+1): #range(1,n+1):1부터 n까지의 숫자 범위
    result *= i
print(result)