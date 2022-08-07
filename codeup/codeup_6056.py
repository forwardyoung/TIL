a, b = input().split()
a = bool(int(a))
b = bool(int(b))
print((a and (not b)) or ((not a)) and b) # a와 b의 bool값이 서로 다를 때