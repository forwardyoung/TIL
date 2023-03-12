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

