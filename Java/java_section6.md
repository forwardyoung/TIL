# 조건문

>  특정 조건을 기준으로 무언가를 결정할 때 사용하는 문법

![](https://github.com/forwardyoung/TIL/blob/master/Java/Java.assets/6-1.png)

## if문

> 특정 동작의 수행 여부를 결정할 때 사용

- 특정 동작을 실행 하거나 하지 않는다. (참이면 수행, 거짓은 생략)

```java
if ( 조건식 ) {
  // 조건식이 참이면 수행할 내용 
}
```

```java
if ( 덥다면? ) {
    에어컨을 튼다!
}
```

활용 예)

```java
// 변수 생성
int number = 102;
// number가 100이상이면?
if (number >= 100) {
  // 해당 number를 출력!
  System.out.println(number);
}
```

### 예제

19세 이상만 캔맥주를 살 수 있도록 `order()` 메소드를 완성하여, 다음과 같은 결과를 얻으시오.

```
19세, 성인인증 완료 => 캔맥주가 나왔습니다.
20세, 성인인증 완료 => 캔맥주가 나왔습니다.
```

```java
public class Beer {
  public static void main(String[] args) {
    order(18); // 18세가 캔맥주를 사려 함
    order(19); // 19세..
    order(20); // 20세..
  }

  public static void order(int age) {
    if (age >= 19) { //19세 이상의 조건식
      System.out.printf("%d세, 성인인증 완료 => 캔맥주가 나왔습니다.\n", age);
    }
  }
}
```

## if-else문

> 둘 중 하나를 선택할 때 사용 (양자 택일)

```java
if ( 조건식 ) {
  // A: 참인 경우 수행!
} else {
  // B: 거짓 인경우 수행!
}
```

```java
if (날씨가 추우면) {
    따뜻한 라떼 주문!
} else {
    시원한 음료 주문!
}
```

활용 예)

```java
// 변수 생성
boolean hungry = false;
// 조건문 실행
if (hungry) {
  System.out.println("배고파, 밥먹자!");
} else {
  System.out.println("음.. 간단히 샐러드 먹자!");
}
```

### 예제

주어진 코드의 buy() 메소드로, 입력 나이에 따른 담배 구매 여부를 출력하려 한다.

다음과  같은 결과가 나올 수 있도록, buy() 메소드의 if-else 구문을 완성하시오.

```
15세 => 담배판매(X)
19세 => 담배판매(O)
22세 => 담배판매(O)
```

```java
public class Tobacco {
  public static void main(String[] args) {
    buy(15); // 15세, 담배 구매 시도
    buy(19); // 19세..
    buy(22); // 22세..
  }

  public static void buy(int age) {
    // 변수 생성
    String result = "";

    // 조건에 따른 결과 생성
    if(age >= 19) {
      result = "O"; // 19세 이상은 판매 허용
    } else {
      result = "X"; // 19세 미만은 판매 금지
    }

    // 결과 출력
    System.out.printf("%d세 => 담배판매(%s)\n", age, result);
  }  
}
```

## else-if문

> 여러 가지 선택지 중 하나를 고를 때 사용

- 기존의 if-else 문 사이에 else-if 문을 추가

```java
if ( 90점보다 큼? ) {
    A학점!
} else if ( 80점보다 큼? ) {
    B학점!
} else {
    그 외 C학점!
}
```

```java
// A, B, C, F 학점을 주는 예
if (score >= 95) { // 95점 이상
  grade = "A";
} else if (score >= 90) { // 90점 이상
  grade = "B";
} else if (score >= 80) { // 80점 이상
  grade = "C";
} else {
  grade = "F";
}
```

### 예제

다음과 같이 나이에 따른 연령대가 나타나도록, 코드를 완성하시오.

- 성인: 만 18세 이상
- 청소년: 만 13세 이상
- 어린이: 만 6세 이상
- 유아: 만 5세 이하

```
22살 => 성인입니다.
16살 => 청소년입니다.
10살 => 어린이입니다.
4살 => 유아입니다.
```

```java
public class BusCard {
  public static void main(String[] args) {
    printRole(22); // 22살 => 성인
    printRole(16); // 16살 => 청소년
    printRole(10); // 10살 => 어린이
    printRole(4); // 4살 => 유아
  }
  
  public static void printRole(int age) {
    // 변수 생성
    String role = "";
    
    // 조건별 결과 선택
    if (age >= 18) {
      role = "성인";
    } else if (age >= 13) {
      role = "청소년";
    } else if (age >= 6){
      role = "어린이";
    } else {
      role = "유아";
    }
    
    // 결과 출력
    System.out.printf("%d살 => %s입니다.\n", age, role);
  }
}
```

## 비교/논리 연산자

### 비교 연산자

> 좌우 값의 크기를 비교하여 참/거짓을 반환

`==` : 같은가?

`!=` : 같지 않은가?

`>` : 큰가?

`>=` : 크거나 같은가?

`<` : 작은가?

`<=` : 작거나 같은가?

```java
// 비교 연산자 코드 예
System.out.println(7 > 4); // true
System.out.println(3 == 5); // false
System.out.println(5 != 10); // true
```

### 논리 연산자

> 논리 연산자는 좌우 논리값(참/거짓)을 통해 새로운 논리값(참/거짓)을 반환

- AND(`&&`)
- OR(`||`)

```java
// AND 연산자 - 양쪽 모두 만족하면, 참!
System.out.println(true && true); // true
System.out.println(true && false); // false
System.out.println(false && true); // false
System.out.println(false && false); // false
// OR 연산자 - 하나라도 만족하면, 참!
System.out.println(true || true); // true
System.out.println(true || false); // true
System.out.println(false || true); // true
System.out.println(false || false); // false
```

### 활용

```java
// 변수 생성
double tall = 182;
// 조건문 처리 - 키가 176cm 이상이면서 185cm이하라면?
if ((tall >= 176)) && (tall <= 185)) {
  System.out.println("♥︎_♥︎");
} else {
  System.out.println("-_-?");
}
```

수학과 영어의 점수가 모두 90점 이상이라면, 전액 장학금을! 한 과목만 90점 이상인 경우, 반액 장학금을 수여하려 한다. 아래 학생들의 성적과 주어진 코드를 참고하여, 출력 예와 같은 결과를 만드시오.

- Park: 수학(100), 영어(92)
- Kim: 수학(82), 영어(96)
- Choi: 수학(82), 영어(88)

**출력 예**

```
Park => 전액 장학금!
Kim => 반액 장학금!
Choi => 다음 기회에~
```

```java
public class Scholarship {
  public static void main (String[] args) {
    // 메소드 호출
    printTest("Park", 100, 92); // Park => 전액 장학금!
    printTest("Kim", 82, 96); // Kim => 반액 장학금!
    printTest("Choi", 82, 88); // Choi => 다음 기회에~
  }
  
  public static void printTest(String name, int math, int eng) {
    // 변수 생성
    String result = "";
    
    // 조건에 따른 값 변경
    if ((math >= 90) && (eng >= 90)) {
      result = "전액 장학금!";
    } else if ((math >= 90) || (eng >= 90)) {
      result = "반액 장학금!";
    } else {
      result = "다음 기회에~";
    }
    
    // 결과 출력
    System.out.printf("%s => %s\n", name, result);
  }
}
```

## 중첩된 조건문

```java
// 변수 생성
double weight = 50.6; // 50.6kg
boolean isMale = false; // 여성
// 남자?
if (isMale) {
  // 몸무게 평균 이상?
  if (weight >= 68.6) {
    System.out.println("남성 평균 몸무게 이상!");
  } else {
    System.out.println("남성 평균 몸무게 미만!");
  }
} else {
  // 몸무게 평균 이상?
  if (weight >= 56.5) {
    System.out.println("여성 평균 몸무게 이상!");
  } else {
    System.out.println("여성 평균 몸무게 미만!");
  }
}
```

### 예제

주어진 코드와 아래의 성인 남여 평균 키 기준을 통해, 평균 이상/미만 여부를 구분하려 한다. 출력 예와 같은 결과를 얻도록, 코드를 완성하시오.

#### 성인 남/여 평균 키

- 남성 평균 키: 173.5cm
- 여성 평균 키: 160.8cm

**출력 예**

```
176.3cm, 남 => 평균키 이상
162.7cm, 여 => 평균키 이상
171.8cm, 남 => 평균키 이하
158.4cm, 여 => 평균키 이하
```

```java
public class AverageHeight {
  public static void main(String[] args) {
    test(176.3, true);  // 176.3cm, 남 => 평균키 이상
    test(162.7, false); // 162.7cm, 여 => 평균키 이상
    test(171.8, true);  // 171.8cm, 남 => 평균키 이하
    test(158.4, false); // 158.4cm, 여 => 평균키 이하
  }
  
  public static void test(double height, boolean isMale) {
    // 변수 생성
    String gender = "";
    String result = "";

    // 조건 처리
    if (isMale) {
      gender = "남";
      if (height >= 173.5) {
        result = "이상";
      } else {
        result = "이하";
      }
    } else {
      gender = "여";
      if (height >= 160.8) {
        result = "이상";
      } else {
        result = "이하";
      }
    }

    // 결과 출력
    System.out.printf("%.1fcm, %s => 평균키 %s\n", height, gender, result);
  }
}
```

## 리뷰 문제

윤년이란 1년이 366일인 해로서 아래와 같은 규칙을 갖는다.

- 기본 적으로 년수가 4의 배수이면 윤년이다
- 그러나 100으로 나누어지는 떨어지는 경우 윤년이 아니다.
- 특별히 1000으로 나누어 떨어지는 경우에는 윤년이 된다.

윤년을 판별하는 코드를 완성하여, 출력 예와 같은 결과를 얻으시오.

**출력 예**

```
1988년은 윤년입니까? true
```

```java
public class LeapYear {
  public static void main(String[] args) {
    /* 1. 입력값 받기 */
    int input = Integer.parseInt(args[0]); // "1988" => 1988
    /* 2. 윤년 여부 계산 */
    boolean judge = isLeapYear(input); // 1988 => true
    /* 4. 결과 출력 */
    System.out.printf("%d년은 윤년입니까? %s", input, judge);
  }
  
  /* 3. 윤년 여부를 반환하는 메소드 */
  public static boolean isLeapYear(int year) {
    // 변수 생성
    boolean result = false;
    
    // 조건문 처리
    if ((year % 4) == 0) {
      result = true;
      if ((year % 100) == 0) {
        result = false;
        if ((year % 1000) == 0) {
          result = true;
        }
      }
    }
    
    // 결과값 반환
    return result;
  }
}
```

