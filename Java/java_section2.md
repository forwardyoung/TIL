## 자바의 특징

1. 많이 쓰이는 언어
2. 멀티 플랫폼 언어 : 자바로 작성된 코드는 다양한 운영체제(UNIX, Window, MacOS, Android, etc..)에서 변경없이 동작
3. 객체지향 언어

> 객체 지향 프로그래밍 (Object-Oriented Programming, OOP) 이란?
>
> :  프로그래밍에서 필요한 데이터를 추상화 시켜 `상태와 행위를 가진 객체`로 만들고, 객체들간의 상호작용을 통해 로직을 구성하는 프로그래밍 방법

- 객체 지향 프로그래밍의 장점
  - 프로그램을 유연하고 변경이 용이하게 만든다.
  - 프로그램의 개발과 보수를 간편하게 만든다.
  - 직관적인 코드 분석을 가능하게 한다.



## 변수

하나의 값(data)를 저장하기 위해 프로그램에 의해 **'이름을 할당 받은 메모리 공간'** 이다.



\- 기본 타입 변수 (primitive type) : 정수형, 실수형, 논리형

\- 참조 타입 변수 (reference type) : 문자열, 배열 등..



## 문자열 변수

```java
// 문자열(String)을 위한 변수, food 생성
String food;

food = "피자";

System.out.println(food); // "피자" 출력
```

```java
public class Greetings {
  public static void main(String[] args) {
    // 문자열(String) 변수 name 만들기
    String name;

    // 변수 name에 특정 값 저장하기
    name = "차밍";

    // 결과 출력
    System.out.println("안녕하세요~ 반갑습니다! 제 이름은,");
    System.out.println(name);
    System.out.println("입니다. 잘 부탁드립니다~");
  }
}

/* 
안녕하세요~ 반갑습니다! 제 이름은,
차밍
입니다. 잘 부탁드립니다~
*/
```



## 정수형 변수

`정수(integer)` : -1, 0, 1, 2, … 와 같이 딱 떨어지는 수 

```java
// 정수(int)를 위한 변수 생성
int age;
// 정수 값 저장(대입)
age = 20;
// 정수형 변수 age의 값 출력
System.out.println(age); // 20
```

```java
  public class Exam {
  public static void main(String[] args) {
    // 정수형 변수 생성
    int midScore; // 중간점수
    int finalScore; // 기말점수

    // 변수에 값 대입
    midScore = 68;
    finalScore = 88;

   // 결과 출력
    System.out.println("밍이의 중간점수:");
    System.out.println(midScore);
    System.out.println("밍이의 기말점수:");
    System.out.println(finalScore);
  }
}

/*
밍이의 중간점수:
68
밍이의 기말점수:
88
*/
```



## 실수형 변수

(**자바에서는 실수 연산은 기본적으로 double 타입으로 처리한다.**)

```java
// 실수형(double) 변수 만들기
double weight;
// 실수 값 대입하기
weight = 50;
// 실수형 변수 weight의 값 출력
System.out.println(weight);
```



```java
public class Avengers {
  public static void main(String[] args) {
    // 실수형 변수 rating 만들기
    double rating;
    
    // 실수 값 대입하기
    rating = 9.82;
    
    // 결과 출력
    System.out.println("어벤져스4 평점:");
    System.out.println(rating);
  }
}

/*
어벤져스4 평점:
9.82
*/	
```



## 논리형 변수

- 논리형(`boolean`)은 참(true) 또는 거짓(false)을 표현

```java
// 논리형 변수 생성
boolean isMale;
// 참/거짓 값 대입
isMale = false;
// 논리형 변수 isMale의 값 출력
System.out.println(isMale);
```



❔ 탕수육 찍먹과 부먹?

```java
public class TangSoo6 {
  public static void main(String[] args) {
    // 논리형 변수 생성
    boolean isBoomuk;
    
    // 논리 값 대입
    isBoomuk = true;
    
    // 결과 출력
    System.out.println("당신은 부먹파입니까?");
    System.out.println(isBoomuk);
  }
}

/*
당신은 부먹파입니까?
true
*/
```



📢 **변수와 문자열 연결하기**

```java
String food = "족발";
int price = 35000;
double weight = 1.25;
boolean isTasteGood = true;

System.out.println("가격: " + price + "원");
// => "가격: 35000원"
```



### 참고

- [변수 (variable)](https://wikidocs.net/81370)

- [객체지향 프로그래밍이란?](https://jongminfire.dev/%EA%B0%9D%EC%B2%B4%EC%A7%80%ED%96%A5-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D%EC%9D%B4%EB%9E%80)
- [객체 지향 프로그래밍(OOP : Object Oriented Programming) 개념 및 활용 정리](https://medium.com/cyranocoding/%EA%B0%9D%EC%B2%B4-%EC%A7%80%ED%96%A5-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D-oop-object-oriented-programming-%EA%B0%9C%EB%85%90-%EB%B0%8F-%ED%99%9C%EC%9A%A9-%EC%A0%95%EB%A6%AC-bd4bc22e4c0b)