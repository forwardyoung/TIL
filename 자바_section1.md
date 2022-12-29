## 자바 프로그래밍

![image-20221229141337485](C:\Users\726jo\AppData\Roaming\Typora\typora-user-images\image-20221229141337485.png)

- `println()` 메소드 : 소괄호 안의 **문자열을 출력**한다.

```java
/* 1. 클래스를 작성하세요. */
public class name {
  /* 2. 메인 메소드를 추가하세요. */
  public static void main(String[] args) {
    /* 3. 자기소개를 출력하세요. */
    System.out.println("안녕하세요. 반갑습니다.");
    System.out.println("저는 차밍입니다. 잘 부탁드립니다.");
  }
}
```



- 주석(comment)

  `//` (한 줄 주석) : 글자 앞쪽에 슬래시를 두 번 쓴다.

  `/* */` (블럭 주석) : 글자 앞뒤를 /와 *로 감싼다.

```java
public class Hello {
  public static void main(String[] args) {
    System.out.println("Hello World!");
    System.out.println("Hi, Java!");
//    System.out.println("Bye, Java!");
  }
}

출력
Hello World!
Hi, Java!
```



> 클래스란?
>
> : 자바 프로그램의 최소 단위로 자바 프로그램은 적어도 하나의 클래스를 가지며, 그 구조는 아래와 같다.

```java
// 이름이 Pizze인 클래스
public class Pizza {
  // 클래스 내부 생략..
}
```



> 메인 메소드란?
>
> : 프로그램 실행의 시작점으로, 클래스 내부에 위치하며, 아래와 같은 구조를 갖는다.

```java
// Pizza 클래스 - 프로그램의 최소 단위
public class Pizza {
  // 메인 메소드 - 프로그램 실행의 시작점
  public static void main(String[] args) {
    // 실행될 코드들..
  }
}
```

