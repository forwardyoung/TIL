## 메소드

자판기에 돈을 넣으면, 음료가 나온다.

햄버거 세트 메뉴도 번호만 알려주면 주문이 된다.

![image-20230301135733058](C:\Users\726jo\AppData\Roaming\Typora\typora-user-images\image-20230301135733058.png)

프로그래밍 또한 마찬가지

![image-20230301140032988](C:\Users\726jo\AppData\Roaming\Typora\typora-user-images\image-20230301140032988.png)

> 일련의 코드를 단순화한 문법을 **메소드**(methods)라고 한다.

### 메소드 호출

- 만들어진 메소드를 실행하는 것

```java
double x = Math.abs(-9.81); // 9.81
```

`abs()` : 절대값을 반환하는 메서드

```java
long y = Math.round(10.4); // 11
```

`round()` : 지정된 값을 가장 가까운 int 혹은 long 값으로 반올림하여 반환하는 메서드

### 메소드 정의

메소드가 호출되기 위해서는 메소드가 정의돼 있어야 한다.

**메소드 구조**

1️⃣메소드명(methods name) : 호출 시 사용

2️⃣입력 변수(parameter) : 입력 값 저장

3️⃣반환 값(return value) : 반환될 값

4️⃣반환 타입(return type) : 반환 값의 타입 

```java
public static 4️⃣ 1️⃣ (2️⃣) { // 입력값 받기
    ~~~~ // 변수 생성
    ~~~~~~~ // 값 계산
    3️⃣ // 값 반환    
}
```

**정수값의 제곱을 반환하는 메소드**

```java
int z = square(3); // 9
```

1) 1️⃣메소드명을 `square`로 작성한다.

```java
public static 4️⃣ square(2️⃣) {
  ...
  return 3️⃣;
}
```

2. 메소드 실행에 필요한 정보(입력되는 정수 3)를 받기 위해 2️⃣파라미터(입력 변수) `int n`을 추가한다.

```java
public static 4️⃣ square(int n) {
  ...
  return 3️⃣;
}
```

3. 제곱값을 만들기 위한 일련의 코드를 작성하고, 최종 3️⃣반환 값을 지정한다.

```java
public static 4️⃣ square(int n) {
  int result; // 변수 생성
  result = n * n; // 값 계산
  return result; // 값 반환
}
```

4. 반환 값의 4️⃣타입을 정의한다.

```java
public static int square(int n) {
  int result;
  result = n * n;
  return result;
}
```

➡️ `square()` 메소드는 아래와 같이 호출 가능

```java
int z = square(5); // 입력: 5 => 반환: 25
System.out.println(z); // 25
```

