numbers = [0, 20, 100, 50, -60, 50, 100]
numbers = list(set(numbers))

result = numbers[0]
for i in numbers:
    if i > result:
        result = i

numbers.remove(result)

result = numbers[0]
for i in numbers:
    if i > result:
        result = i
print(result)