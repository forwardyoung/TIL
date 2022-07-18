# while 문으로 풀 때
n = 0
result = 0
user_input = int(input())

while n <= user_input:
    result += n
    n += 1
print(result)

# for 문으로 풀 때
n=10
result=0
for i in range(n+1):
    result += i
print(result)