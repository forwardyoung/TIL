# 타입과 형 변환

**⚠️ 나눗셈 연산 주의**

- int와 int의 연산 결과는 int
-  double과 int의 연산은 double

➡️ 숫자간 연산은 더 큰 타입을 따른다.

```java
double a = 5.0 / 2.0; // 2.5
int b = 4 / 2;        // 2
int c = 5 / 2;        // 2.5 (X) => 2 (O)
```



**⚠️ 타입 불일치 주의**

- 변수에 값 대입 시, 그 값이 변수의 타입과 일치해야 한다.

```java
// 타입 불일치 에러
int score = "100";

// 해결 방법
int score = 100;      // int로 일치
String score = "100"; // String으로 일치
int score = Integer.parseInt("100"); // "100" => 100
```



**⚠️ 타입 변환 주의**

- 타입 불일치의 문제는 타입 변환을 통해 해결가능하다. 

1 ) 자동 변환 : int는 double로 대입될 수 있다. 2를 2.0으로 보아도 무방하다. 이러한 자동 변환은 **더 큰 타입으로 대입 시 발생**한다.

(byte(1) < short(2) < int(4) < long(8))

```java
// 자동 변환 (더 큰 타입으로 대입될 때)
double p = 2;  // 2 => 2.0
int n = 5 / 2; // 2
double q = n;  // 2 => 2.0
```

2 ) 직접 변환 : 거꾸로 double은 int로 대입될 수 없다. 

제로 소수점을 버리고 정수로 만들 순 있다. ➡️ **타입 캐스팅(casting)**

```java
// 에러 발생
int r = 10.4; // ERROR

// 실수를 정수로 강제 캐스팅
int r = (int) 10.4; // 10.4 => 10
```



# printf(), 숫자 출력

> 출력을 위한 문자열에 값을 삽입시켜 출력

```java
System.out.printf("차밍이의 나이는 %d세입니다.", age);
```

`%d` : 정수 타입으로 삽입

```java
// 변수 생성
int month = 2;
int day = 14;

// 결과 출력 => "제 생일은 2월 14일입니다."
System.out.printf("제 생일은 %d월 %d일입니다.", month, day);
```

 정수형 변수 month와 day는, 문자열 속 %d에 차례로 삽입되어 출력된다.

```java
public class StringInterpolation2 {
  public static void main (String[] args) {
    // 변수 생성
    int a = 6 / 2;
    int b = 7 / 2;

    // 결과 출력 a = 3, b = 3
    System.out.printf("a = %d, b = %d", a, b); 
      
  }
}
```



`%f` : 실수 값 삽입

```java
// 변수 생성
double pi = 3.14;

// 결과 출력 => "파이의 값은 3.140000 입니다."
System.out.printf("파이의 값은 %f 입니다.", pi);
```

```java
public class StringInterpolation3 {
  public static void main (String[] args) {
    // 변수 생성
    double x = 7.0 / 2.0; // 3.5
    double y = 7 / 2; // 3 => 정수와 정수의 연산(자동 변환) => 3.0

    // 결과 출력
    System.out.printf("x = %f, y = %f", x, y);
  }
}
```

📍 소수점 이하 자릿 수 설정

```java
// 소수점 이하 2자리까지 출력 => 3.14
double pi = 3.14159265;
System.out.printf("%.2f\n", pi);

// 소수점 이하 5자리까지 출력 => 3.14159
double pi = 3.14159265;
System.out.printf("%.5f\n", pi);
```



`%s` : 문자열 삽입

```java
// 변수 생성
String name = "홍팍";
String hobby = "산책하기";

// 결과 출력 => "이름: 홍팍 취미: 산책하기"
System.out.printf("이름: %s ", name);
System.out.printf("취미: %s", hobby);
```

`\n` : 줄바꿈



- **casting**

```java
public class Casting {
  public static void main(String[] args) {
    // 변수 생성
    double tall = 176.4;
    double weight = 82.34;
    
    /* 1. 실수형 변수를 정수로 캐스팅하여 출력하시오. */
    System.out.printf("신장: %dcm\n", (int) tall);
    System.out.printf("체중: %dkg\n", (int) weight);
  }
}
```



- 문자열을 정수로

```java
// 형변환: 문자열(String) => 정수(int)
int a = Integer.parseInt(three); // "3" => 3
int b = Integer.parseInt(seven); // "7" => 7
// 결과 출력 => 10
System.out.println(a + b);
```

- 문자열을 실수로

```java
// 변수 생성
String pi = "3.14";
// 형변환: 문자열(String) => 실수(int)
double c = Double.parseDouble(pi); // "3.14" => 3.14
```

```java
public class StringToNumber {
  public static void main(String[] args) {
    // 변수 생성
    String strSeven = "7";
    String strPi = "3.14";
    
    // 형변환: 문자열 => 숫자
    int a = Integer.parseInt(strSeven);
    double b = Double.parseDouble(strPi);
    
    // 숫자 계산
    double c = a + b;
    
    // 결과 출력 7 + 3.14 = 10.14
    System.out.printf("%d + %.2f = %.2f", a, b, c);
      
  }
}
```



`Match` 클래스 : 수학에서 사용되는 변수 및 함수들 제공

```java
// 원주율 - Math.PI
double pi = Math.PI; // 3.14159265..

// 절대값 - Math.abs();
double x = Math.abs(-9.81); // 9.81

// 반올림 - Math.round();
long n = Math.round(10.6); // 11
```



원의 반지름 입력 받았을 때, 다음과 같이 출력된다.

`반지름이 4인 원의 넓이 => 50.265`

```java
public class CircleAreaCalculator {
  public static void main(String[] args) {
    /* 1. 입력값 받기 */ 
    int r = Integer.parseInt(args[0]); // "4" => 4
    
    /* 2. 원의 넓이 계산 */
    double s = Math.PI * r * r;
    
    /* 3. 결과 출력 */
    System.out.printf("반지름이 %d인 원의 넓이 => %.3f", r, s);
    
  }
}
```



