# 변수와 타입, 그리고 연산자

> 변수 (variables)
>
> : 변하는 수로서, 이름 붙여진 메모리 공간

- 생성된 변수는 새로운 값으로 변경될 수 있다.

```java
public class HellWorld {
  public static void main(String[] args) {
    // 변수 생성 및 초기값 설정
    String message = "헬로 월드!";
    
    // 변수값 출력
    System.out.println(message);
    
    /* 변수 값을 변경하세요 */
    message = "웰컴 투 헬!";
    
    // 변수값 출력
    System.out.println(message);
  }
}

/* 출력 
헬로 월드!
웰컴 투 헬!
*/
```



> 타입 (types)
>
> : 변수의 형태
>
> ⚠️ 기본형과 레퍼런스형으로 나뉜다.



## 연산자 (operators)

```java
int result = 3 + 8 * (3-1);
```

🕹️ **우선 순위**

1) 괄호 먼저
2) 곱셈 or 나눗셈
3) 덧셈 or 뺄셈
4) 대입

 ⚠️같은 우선순위의 경우, 왼쪽 ➡️ 오른쪽

```java
public class DoMath {
  public static void main(String[] args) {
    // 변수 생성 및 초기화
    double score = 1.0 + 2.0 * (3.0 + 4.0) - 5.0;
    
    // 변수값 출력
    System.out.println(score);
    
    // 변수값 변경
    score = score / 2.0;
    
    // 변수값 출력
    System.out.println(score);
    
    /* score 변수가 2.5가 되도록 빈칸을 채우세요. */
    score = score / 2.0;
    
    // 변수값 출력
    System.out.println(score);
  }
}

/* 출력
10.0
5.0
2.5
*/
```



## 변수값 복사 & 문자열 연결

- 변수의 값은 대입연산을 통해 복사될 수 있다.

```java
// 변수 생성 및 값 초기화
double origin = 3.14;

// 변수 값 복사
double copy = origin;

// 변수 값 출력
System.out.println(copy); // 3.14
```

- 문자열은 덧셈(`+`) 연산을 통해, 다른 문자열과 연결할 수 있다.

```java
// 문자열 변수 생성
String a = "AAA";
String b = "bbbb";
// 문자열 연결을 통한 새 문자열 생성
String c = a + b;
// 새 문자열 c를 출력
System.out.println(c); // AAAbbbb
```



❔다음과 같이 출력하려면?

```
가나다라
가나다라마바사
```

```java
public class Copy {
    public static void main(String[] args) {
        // 문자열 생성
		String origin  = "가나다라";
        
       	// 문자열 복사
        String copy = origin; 
        
        // 문자열 출력
        System.out.println(copy); // 가나다라
        
        /* 덧셈연산을 통해 원하는 문자열을 연결 */
        copy = copy + "마바사";
        
        // 결과 출력
    	System.out.println(copy); // 가나다라마바사
    }
        
}
```



## 문자열과 숫자 연결

```java
// 정수(int)와 문자열 연결
int hour = 13;
System.out.println("지금은 " + hour + "시");
// => "지금은 13시"

// 실수(double)와 문자열 연결
double weight = 1.45;
System.out.println("무게: " + weight + "kg");
// => "무게: 1.45kg"
```



## 문자열과 논리값 연결

```java
boolean hungry = true;
System.out.println("배고파? " + hungry);
// => "배고파? true"
```



❔다음과 같이 출력하려면?

```java
-------------------------
차밍이의 8월 23일 다이어트 일지
-------------------------
식사 횟수: 1회
몸무게: 5.3kg
```

```java
public class StringConcatenation {
    public static void main(String[] args) {
        /* 각 변수의 값 초기화 */
        int month = 8;
        int day = 23;
        int n = 1;
        double weight = 5.3; // 실수형이므로 double
        
        // 결과 출력
        System.out.println("-------------------------");
        System.out.println("차밍이의 " + month + "월 " + day + "일 다이어트 일지");
        System.out.println("-------------------------");
        System.out.println("식사 횟수: " + n + "회");
        System.out.println("몸무게: " + weight + "kg");
    }
}
```



## 입력값 받기

- 입력된 값은 변수 `args[0]`를 통해 사용할 수 있다.

`입력` : 콜라

```java
public class ChickenDrinks {
  public static void main (String[] args) {
    System.out.println("치킨엔 " + args[0] + "가 제맛이지~");
  }
}
```

`출력` : 치킨엔 콜라가 제맛이지~



- 입력값이 둘 이상인 경우, 첫 입력값은 `args[0]`, 두번째 입력값은 `args[1]`, ...의 순으로 입력된다.

- 입력값은 공백문자(space, enter, ...)로 구분된다.



`입력` : 참치마요 돈까스

```java
public class KimBob {
  public static void main(String[] args) {
    System.out.println(args[0] + "김밥");
    System.out.println(args[1] + "김밥");
  }
}
```

```
출력

참치마요김밥
돈까스김밥
```



⚠️ 사용자 입력값은 모두 **문자열**이므로 숫자 계산을 할 수 없다.

`입력` : 123 3.14

```java
public class Lab03Review {
  public static void main(String[] args) {
    System.out.println(args[0] + args[1]);
    // 1233.14
  }
}
```



- 입력값을 **숫자로 변경**해야 숫자 계산을 할 수 있다.

```java
// 문자열을 정수(int)로 변환: "123" => 123
int a = Integer.parseInt(args[0]);

// 문자열을 실수(double)로 변환: "3.14" => 3.14
double b = Double.parseDouble(args[1]);

// 숫자 덧셈 후 출력
System.out.println(a + b); // 126.14
```



`입력` : 77.0

```java
public class Lab03Review {
  public static void main(String[] args) {
    /* 1. 문자열을 실수로 변환하세요. */
    double f = Double.parseDouble(args[0]); // "77.0" => 77.0
    /* 2. 화씨온도를 섭씨로 변환하세요. */
    double c = (f - 32.0) / 1.8;
    /* 3. 결과를 출력하세요. */
    System.out.println("화씨 " + f + "도는 섭씨로 " + c + "도 입니다!");
  }
}

// 출력 : 화씨 77.0도는 섭씨로 25.0도 입니다!
```

