## 메소드

자판기에 돈을 넣으면, 음료가 나온다.

햄버거 세트 메뉴도 번호만 알려주면 주문이 된다.

![](https://github.com/forwardyoung/TIL/blob/master/Java/Java.assets/5-1.png)

프로그래밍 또한 마찬가지

![](https://github.com/forwardyoung/TIL/blob/master/Java/Java.assets/5-2.png)

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

### 단일 파라미터 메소드

> 입력 변수가 하나만 있는 메소드

```java
# 단일 파라미터 메소드 호출 예
int x = square(4); // 입력값: 4 => 반환값: 16
```

- 메소드 호출 시 입력한 값은 입력 변수 즉, 파라미터로 대입된다.

```java
# 단일 파라미터 메소드 정의 예
public static int square(int n) {
  int result = n * n; // 변수 생성 및 제곱 값 대입
  return result; // 값 반환
}
```

**세제곱을 반환하는 cube() 메소드**

```java
public class CubeVolume {
  // 프로그램 실행의 시작점
  public static void main(String[] args) {    
    // 변수 생성
    int n = 3;

    // 메소드 호출을 통한 값 계산
    int x = cube(n);
    
    // 결과 출력
    System.out.printf("%d의 세제곱 => %d", n, x);
  }

  // cube() : 입력값의 세제곱 반환하는 메소드
  public static int cube(int num) {
    // 변수 생성
    int result;
    
    /* 2. 세제곱을 계산하시요 */
    result = num * num * num;
    
    // 값 반환
    return result;
  }
}
/* 
입력 : 3
출력 : 3의 세제곱 => 27
*/
```

### 다중 파라미터 메소드

> 입력 변수가 2개 이상인 메소드

![](https://github.com/forwardyoung/TIL/blob/master/Java/Java.assets/5-3.png)

**원기둥의 부피 구하기**

```java
public class CylinderVolume {
  // 프로그램 실행의 시작점!
  public static void main(String[] args) {
    // 변수 생성
    double r = 7.0;
    double h = 5.0;

    // 부피 계산
    double v = volume(r, h);

    // 결과 출력
    System.out.printf("반지름이 %.1f, 높이가 %.1f인 원기둥의 부피: %.1f", r, h, v);
  }

  // 반지름과 높이를 입력받아 원기둥의 부피를 반환
  public static double volume(double radius, double height) {
    return Math.PI * radius * radius * height; 
  }
}
/*
입력 : 7.0 5.0
출력 : 반지름이 7.0, 높이가 5.0인 원기둥의 부피: 769.7
*/
```

### 타입 불일치 에러

📍입력된 절달과 파라미터의 타입이 일치해야 한다.

```java
# 메소드 호출 예
int x = foo(0.0); // double을 int로 대입 불가
int y = foo("3"); // String을 int로 대입 불가
# 메소드 정의 예
public static int foo(int n) {
  return n + n;
}
```

📍반환값의 타입

```java
// ERROR: 6 => String (X)
String z = foo(3);
```

캐스팅을 사용하여 출력 예와 같은 결과를 얻어보자.

**출력 예** : `a = 9, b = 8`

```java
public class WhatIsWrong {
  public static void main(String[] args) {
    int a = square((int) 3.0); // 3.0 => 3
    int b = (int) cube(2); // 8.0 => 8
    System.out.printf("a = %d, b = %d\n", a, b);
  }

  public static int square(int n) {
    return n * n;
  }

  public static double cube(double n) {
    return n * n * n;
  }
}
```

### 파라미터가 없는 메소드

```java
# 파라미터가 없는 메소드 호출 예
int a = getTen();
# 파라미터가 없는 메소드 정의 예
public static int getTen() {
  return 10;
}
```

- `Math.random()` 메소드 : **0.0** 이상 **1.0** 미만의 임의 실수를 반환

```java
# 파라미터가 없는 메소드 호출 예
double x = Math.random(); // 0.0 <= x < 1.0
```

- `Math.random()` 메소드를 사용하여, 1부터 10 사이의 임의 정수를 구하는 예

```java
double r = 10 * Math.random(); // 0.0 ~ 9.9999
int temp = (int) r; // 0 ~ 9
int n = temp + 1; // 1, 2, 3, ..., 10 중 하나
```

- 1~6 사이의 정수를 반환하는 `rollDie()` 메소드를 완성하여, 출력 예와 같은 결과를 반환하는 문제

**출력 예**

N은 1부터 6사이의 정수

> 주사위의 눈: N

```java
public class Random {
  public static void main(String[] args) {
    // 메소드로부터 값을 반환
    int x = rollDie();
    
    // 결과 출력
    System.out.printf("주사위의 눈: %d", x);
  }
  
  // 1~6 사이의 임의의 정수를 반환
  public static int rollDie() {
    double r = 6 * Math.random(); // => 6 * 0.0 ~ 0.999 = 0 ~ 5.999
    int temp = (int) r; // r을 정수로 casting하면 0 ~ 5 
    int n = temp + 1;
    return n;
  }
}
```

### 리턴값이 없는 메소드

> void는 리턴이 없는 자료형

- **void** 타입 메소드

```java
# 리턴값이 없는 메소드 호출 예
printHello();
# 리턴값이 없는 메소드 정의 예
public static void printHello() {
  System.out.println("Hello");
  return;
}
```

- **return** 키워드 생략

```java
public static void printHello() {
  System.out.println("Hello");
}
```

- 메인 메소드에서 다른 메소드를 호출하여, 출력 예와 같은 결과를 얻어야 한다.

**출력 예**

```
라면을 사온다.
물을 끓인다.
라면을 넣는다.
맛있게 먹는다.
```

```java
public class Ramyun {
  public static void main(String[] args) {
    buy();
    boil();
    put();
    eat();
  }
  
  public static void boil() {
    System.out.println("물을 끓인다.");
  }
  
  public static void buy() {
    System.out.println("라면을 사온다.");
  }
  
  public static void eat() {
    System.out.println("맛있게 먹는다.");
  }
  
  public static void put() {
    System.out.println("라면을 넣는다.");
  }
}
```

### 메소드의 중첩 호출

- 메소드 안에서 또 다시 메소드를 호출할 수 있다.

다음 **threeStar()** 메소드는 내부적으로 **oneStar()**를 3번 호출한다.

```java
# 메소드 정의 예
public static void threeStar() {
  oneStar();
  oneStar();
  oneStar();
}
public static void oneStar() {
  System.out.printf("*");
}

*** // threeStar() 출력 
```

- 다음과 같은 직사각형이 출력되도록 하는 `drawRectangle()` 메소드

```java
* * * * * *
*         *
* * * * * *
```

```java
public class ControlFlow {
  public static void main(String[] args) {
    drawRectangle();
  }

  public static void drawRectangle() {
    /* 직사각형이 그려지도록 해당 메소드를 구현하세요. */
    drawLine(); // 윗변
    drawEdge(); // 중간
    drawLine(); // 밑변
  }

  // 직선을 그리는 메소드
  public static void drawLine() {
    System.out.println("* * * * * *");
  }

  // 양 끝점을 그리는 메소드
  public static void drawEdge() {
    System.out.println("*         *");
  }
}
```

**칼로리 계산 문제**

> 삼겹살 1인분의 무게는 180g이고, 또 삼겹살 1g의 칼로리가 5.179kcal 이다. 이를 참고하여 삼겹살 3인분의 칼로리를 소수점 이하 둘째 자리까지 출력하시오.

```java
public class Pork {
  public static void main(String[] args) {
    int num = 3; // 3인분에 대한 정보를 저장할 수 있는 변수 생성
    double result = calculate(num); // 3인분에 대한 칼로리를 계산하는 메소드 호출
    System.out.printf("삼겹살 %d인분: %.2f kcal", num, result);
  }

  /* 4. 칼로리 계산을 위한 메소드를 작성하시오. */
  public static double calculate(int n) {
    int gram = n * 180; // 1인분은 180g
    double kcal = gram * 5.179; // 3인분을 kcal로 환산
    return kcal;
  }
}

삼겹살 3인분: 2796.66 kcal // 출력
```

