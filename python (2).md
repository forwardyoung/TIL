### 제어문(Control Statement)

- 제어문은 **순서도(flow chart)**로 표현이 가능

  [순서도 예시](https://www.edrawsoft.com/templates/pdf/algorithm-flowchart.pdf)
  
  

### 조건문

: 조건문은 참/거짓을 판단할 수 있는 조건식과 함께 사용

`if expression:`

들여쓰기 네 칸 `print()`

`else:`

들여쓰기 네 칸 `print()`

- expression에는 참/거짓에 대한 조건식
- 조건이 참 - 들여쓰기 되어있는 코드 블럭 실행
- 이외의 경우 else 이후 들여쓰기 된 코드 블럭 실행

**실습 문제**

- num은 input으로 사용자에게 입력을 받으세요.

```python
num = input()
print(num)
```

- 조건문을 통해서 홀수/짝수 여부를 출력하세요.

⚠️ 숫자로서의 num!

➡️ input의 반환값은 항상 문자열의 형태로 반환하기 때문

```python
num = int(input())
if num % 2 == 1:
    print('홀수')
else:
    print('짝수')
```

or

```python
if int(num) % 2 ==1:
    print('홀수')
else:
    print('짝수')
```



### 복수 조건문

: 복수의 조건식을 활용할 경우 elif를 활용하여 표현함

**실습 문제**

- 다음은 미세먼지 농도에 따른 등급일 때, dust 값에 따라 등급을 출력하는 조건식을 작성하시오.

| 좋음 0~30 | 보통 ~80 | 나쁨 ~150 | 매우나쁨 151~ |
| --------- | -------- | --------- | ------------- |

```python
dust = 100
# dust가 150보다 크면, 매우 나쁨
if dust > 150:
    print('매우 나쁨')
# 80보다 크면, 나쁨
elif dust > 80:
    print('나쁨')
# 30보다 크면, 보통
elif dust > 30:
    print('보통')
# 좋음
else:
    print('좋음')
print('미세먼지 확인 완료')
```

⚠️ else는 위의 모든 조건에 해당하지 않는 나머지의 경우이기에 별도의 조건은 불가능

⚠️ 조건문에서 else는 생략이 가능



### 중첩 조건문

**실습 문제**

- 중첩조건문을 활용하여 미세먼지 농도(dust 값)이  음수인 경우 '값이 잘못 되었습니다'를 출력하시오.

```python
dust = -10

if dust > 150:
    print('매우 나쁨')
elif dust > 80:
    print('나쁨')
elif dust > 30:
    print('보통')
else:
    if dust < 0 :
        print('음수 값입니다.')
    else:
        print('좋음')
```

or

```python
dust = -10

if dust > 150:
    print('매우 나쁨')
elif dust > 80:
    print('나쁨')
elif dust > 30:
    print('보통')
elif dust > 0:
    print('좋음')
else:
    print('음수 값입니다.')
```

- 중첩조건문을 활용하여 미세먼지 농도(dust 값)이 300이 넘는 경우 '실외 활동을 자제하세요'를 추가적으로 출력하고

  음수인 경우 '값이 잘못 되었습니다'를 출력하시오. 

```python
dust = 1000

if dust > 150:
    if dust > 300:
        print('실외활동을 자제하세요')
    print('매우 나쁨')
elif dust > 80:
    print('나쁨')
elif dust > 30:
    print('보통')
else:
    if dust < 0:
        print('음수 값입니다.')
    else:
        print('좋음')
```



### 조건 표현식(Conditional Expression)

: 일반적으로 조건에 따라 값을 할당하려고 할 때 활용

**실습 문제**

- num이 정수일 때 다음 코드의 의미는?

`value = num if num >= 0 else -num`

코드 의미 : 참일 경우 num을 출력, 거짓일 경우 -num을 출력

➡️ 절대값

- 다음의 코드와 동일한 조건문을 작성하시오.

```python
num = -5
value =num if num >= 0 else 0
print(value)
```

```python
num = -5
if num >= 0:
    value = num
else:
    value = -num
print(value)    
```



### 반복문

✔️ while 문

: 조건식이 참인 경우 반복적으로 코드를 실행

- 코드 블록이 모두 실행되고, 다시 조건식을 검사하며 반복적으로 실행됨
- while문은 무한 루프를 하지 않도록 종료 조건이 반드시  필요

```python
a = 0
while a < 5:
    print(a)
    a += 1
print('끝')    
```

➡️ 위의 경우 while문 코드는 총 6번 실행될 것

**실습 문제**

- 1부터 사용자가 입력한 양의 정수까지의 총합을 구하는 코드를 작성하시오.
  - n이 1씩 증가
  - result에는 n을 더해야 함
  - 종료는 n이 user_input보다 커지면 ➡️ true는 작거나 같을 때

```python
#처음 시작 값
n = 0
# 0부터 더하기 위해서
result = 0
# user_input 값
user_input = int(input())

while n <= user_input:
    result += n
    n += 1
print(result)
```

---

✔️ for 문

:  시퀀스(string, tuple, list, range)를 포함한 순회가능한 객체(iterable) 요소를 모두 순회함

- 처음부터 끝까지 모두 순회하므로 별도의 종료조건이 필요하지 않음

```python
for fruit in ['apple', 'mango', 'banana']:
    print(fruit)
print('끝')
```

➡️ 통(iterable)에 있는 것을 하나씩 꺼내서 변수명에 넣어 줌

**문자열 순회**

- 사용자가 입력한 문제를 range를 활용하여 한 글자씩 세로로 출력하시오.

```python
chars = input()
# hi 입력
for idx in range(len(chars)):
    print(chars[idx])
# h
# i 출력
```

**딕셔너리 순회**

- 기본적으로 key를 순회하며, key를 통해 값을 활용

```python
grades = {'john' : 80, 'eric' : 90}
for name in grades:
    print(name)

john
eric
```

```python
grades = {'john' : 80, 'eric' : 90}
for name in grades:
    print(name, grades[name])
    
john 80
eric 90
```

---

✔️ 반복문 제어

- break : 반복문을 종료

```python
# case 1)
n = 0
while True:
    if n == 3:
        break
    print(n)
    n += 1
#출력값 다음과 같음
0
1
2

# case 2)
for i in range(10):
    if i > 1:
        print('0과 1만 필요해!')
        break
    print(i)
#출력값 다음과 같음
0
1
0과 1만 필요해!
```

⚠️ break를 만나면 종료

```python
for i in range(6):
#range(6)은 i값이 0~5까지    
    if i % 2 == 0:
        continue
    print(i)
    
#출력값 다음과 같음    
1
3
5
```

⚠️ continue를 만나면, 이후 코드인 print(i)가 실행되지 않고 바로 다음 반복을 실행

- for-else
  - 모든 반복을 하게 되면 else문 실행
    - break를 통해 중간에 종료되는 경우 else문은 실행되지 않음

```python
for char in 'apple':
    if char == 'b':
        print('b!')
        break
else:
    print('b가 없습니다.')
    
# 출력 : b가 없습니다.
```

```python
for char in 'banana':
    if char == 'b':
        print('b!')
        break
else:
    print('b가 없습니다.')
    
# 출력 : b!
```



[📍유용한 사이트](https://pythontutor.com/)

