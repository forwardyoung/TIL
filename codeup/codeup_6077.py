n = int(input())
sum = 0
for i in range(n+1): # n까지 포함시키기 위해 1을 더한다.
    if i%2 == 0:
        sum += i
print(sum)