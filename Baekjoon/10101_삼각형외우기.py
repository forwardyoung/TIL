a = int(input())
b = int(input())
c = int(input())

if (a + b + c) == 180: # 세 각의 합이 180(삼각형일 때)
    if a == b == c == 60: # 세 각의 크기가 모두 60인 것도 결국 세 각의 합이 180이므로 
        print('Equilateral')
    elif a != b and b != c and c != a: # a~c 모두 다를 때
        print('Scalene')
    else: # 합이 180이고 위의 두 경우를 제외하면 두 각은 같아야 함.
        print('Isosceles')
else: # 세 각의 합이 180이 아닐 때
    print('Error') # 에러 발생