# 반복문

> 규칙적 반복 코드를 단순화하는 문법

**단순 코드**

```java
System.out.println("# 1");
System.out.println("# 2");
///
System.out.println("# 1000");
```

VS

**반복문 코드**

```java
for (int i = 1; i <= 1000, i++) {
    System.out.println("# " + i);
}
```

- while : 반복 횟수가 상황에 따라 다른 경우
- for : 반복 횟수가 명확할 때

⚠️반복문 탈출이 불가능한 무한 루프(∞)에 주의해야 한다.

## while 문

> 조건식이 참인 경우, 반복 내용을 수행한다.
>
> ➡️ 거짓이 될 때까지 계속 수행되므로, 무한 루프에 빠지지 않도록 주의해야 한다.

```java
while (조건식) {
    // 반복 내용
}
```

### 숫자 역순 출력하기

```
4
3
2
1
```

while문을 사용하여 위와 같은 출력 결과를 만들기 위한 코드

```java
// 변수 생성
int n = 4;

// 반복 수행
while (n > 0) { // n의 값이 0보다 크면 반복
    System.out.println(n);
    n--; // n을 1만큼 감소
}
```

### 예제

입력 값이 5일 때, 다음과 같은 출력 결과를 만들어라.

**출력 예**

```
카운트 다운을 시작합니다..
5..
4..
3..
2..
1..
0..
발사!!
```

```java
public class WhileStatement {
  public static void main(String[] args) {
    // 입력값 받기
    int startNum = Integer.parseInt(args[0]); // "5" => 5

    // 카운트 다운 출력
    countDown(startNum);
  }

  public static void countDown(int num) {
    System.out.println("카운트 다운을 시작합니다..");

    while (num >= 0) {
      System.out.printf("%d..\n", num); // 5.. 4..
      num--;
    }

    System.out.println("발사!!");
  }
}
```

## for 문

> for 문이 실행되면 초기설정 부분은 단 한 번 수행되며, 조건식이 참인 경우, 반복 내용을 수행한다. 반복 내용을 다 마치면 매번 갱신영역을 수행한 뒤, 다시 또 조건식을 검사한다. 이러한 실행 흐름은, **조건식이 거짓이 될 때까지** 수행된다.

```
for (초기설정; 조건식; 매회 갱신) {
  // 반복 내용
}
```

### 숫자 증가시켜 출력

```
1
2
3
4
```

for문을 사용하여 위와 같은 출력 결과를 만들기 위한 코드

```java
for (int i = 1; i <= 4; i++) {
    System.out.println(i);
}
```

### 예제

1) for 문을 사용하여, 1부터 N까지 연속된 정수를 출력하려 한다. 7을 입력했을 때 다음과 같은 출력 결과를 만들어라.

**출력 예**

```
출력을 시작합니다..
1 2 3 4 5 6 7 
끝!!
```

```java
public class ForStatement {
  public static void main(String[] args) {
    // 입력값 받기
    int n = Integer.parseInt(args[0]); // "7" => 7

    // 메소드를 통한, 결과 출력
    printNumbers(n);
  }

  // 1부터 N까지, 정수를 출력
  public static void printNumbers(int max) {
    // 출력 시작!
    System.out.println("출력을 시작합니다..");
    
    // 반복을 통한, 숫자 출력 1~max
    for (int i = 1; i <= max; i++) {
      System.out.printf("%d ", i);
    }
    
    // 끝!
    System.out.println("\n끝!!");
  }
}
```

2) 정수 N을 입력하여, 1부터 N까지 정수의 총합을 출력하려 한다. 5를 입력했을 때, 다음과 같은 출력 결과를 얻으시오.

**출력 예**

```
정수의 총합(1~5) => 15
```

```java
public class SumNumbers {
  public static void main(String[] args) {
    // 입력값 받기
    int n = Integer.parseInt(args[0]); // "5" => 5

    // 총합 계산
    int result = sum(n);

    // 결과 출력
    System.out.printf("정수의 총합(1~%d) => %d", n, result);
  }
  
  public static int sum(int max) {
    // 변수 생성
    int sum = 0;

    // 반복 계산: 1 + 2 + ... + max
    for (int i = 1; i <= max; i++) {      
      sum += i;
    }
    // 결과 반환
    return sum;
  }
}
```

## break 문

```java
// 조건식이 참이면, A -> B -> C를 연속적으로 수행
while (조건식) {
  action A
  action B
  action C
}
for (int i = 0; 조건식; i++) {
  action A
  action B
  action C
}
```

만약 A와 B까지만 수행 후, 반복을 탈출하고 싶다면?

➡️ **break** 문을 사용한다.

```java
if (조건식) { // 조건식이 참이면
  break;    // 반복문 탈출!
}
```

```java
// 총합을 위한 변수 생성
int sum = 0;
// 반복 수행
for (int i = 1; i <= 10; i++) {
  // 수행 도중, 반복문 탈출!
  if (i == 4) {
    break;
  }
  // i값을 sum에 더함
  sum += i;
}
// 결과 출력
System.out.println(sum); // 6
```

### 예제

주어진 코드는 1부터 10까지의 합을 출력한다. 이에 break 문을 삽입하여, 출력 예와 같은 결과를 얻으시오.

**출력 예**

```
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
=> 55
```

```java
public class Break {
  public static void main(String[] args) {
    // 1부터 10까지 총합 출력 및 계산
    printSum(1, 10);
  }

  // start부터 end까지의 총합을 출력
  public static void printSum(int start, int end) {
    // 변수 생성
    int sum = 0;

    // 총합 계산
    for (int i = start; i <= end; i++) {
      System.out.printf("%d", i);
      sum += i;

      // end(마지막 숫자)인 경우,
      if (i == end) {
        /* 반복문을 탈출하세요. */
        break;
      }
      
      System.out.printf(" + ");
    }
    
    // 결과 출력
    System.out.printf("\n=> %d", sum);
  }
}
```

## continue 문

```java
// 조건식이 참이면, A -> B -> C를 연속적으로 수행
while (조건식) {
  action A
  action B
  action C
}
for (int i = 0; 조건식; i++) {
  action A
  action B
  action C
}
```

A만 수행 하고 다음 반복으로 넘어가고 싶다면?

➡️ **continume** 문을 사용한다.

```java
if (조건식) { // 조건식이 참이면
  continue; // 다음 반복으로 강제 이동!
}
```

```java
// 총합을 위한 변수 생성
int sum = 0;
// 반복 수행: 1부터 7까지 홀수의 총합
for (int i = 1; i <= 7; i++) {
  // 짝수는 제외!
  if (i % 2 == 0) {
    continue;
  }
  // i값을 sum에 더함
  sum += i;
}
// 결과 출력
System.out.println(sum); // 16
```

### 예제

주어진 코드는 1부터 10까지의 합을 출력한다. continue 문을 추가하여 3의 배수를 제외한 총합을, 출력 예와 같이 만드시오.

**출력 예**

```
1 + 2 + 4 + 5 + 7 + 8 + 10
=> 37
```

```java
public class Continue {
  public static void main(String[] args) {
    printSum(1, 10);
  }
  
  public static void printSum(int start, int end) {
    // 변수 생성
    int sum = 0;

    // 반복 수행
    for (int i = start; i <= end; i++) {
      if (i % 3 == 0) {
        /* 1. 다음 반복으로 넘겨주세요. */
        continue;
      }
      
      System.out.printf("%d", i);
      sum += i;
      
      if (i == end) {
        break;
      }
      System.out.printf(" + ");
    }
    
    // 결과 출력
    System.out.printf("\n=> %d", sum);
  }
}
```

## 중첩 반복문

> 반복문 속에 또 다른 반복문이 들어가는 것

**7행 4열 구조의 별 표시를 출력**

```
* * * * 
* * * * 
* * * * 
* * * * 
* * * * 
* * * * 
* * * * 
```

**복사 붙여넣기 방식**

```java
System.out.println("* * * * ");
System.out.println("* * * * ");
System.out.println("* * * * ");
System.out.println("* * * * ");
System.out.println("* * * * ");
System.out.println("* * * * ");
System.out.println("* * * * ");
```

**반복문 활용**

```java
// 반복 방식 출력(row: 0 ~ 6)
for (int row = 0; row < 7; row++) {
  System.out.println("* * * * ");
}
```

**반복문 속 반복문**

위 코드의 한 행(4개의 별)에 대한 내용을 반복문으로 대체

```java
// 총 7개의 행 출력
for (int row = 0; row < 7; row++) {
  // 행마다 4개의 별 출력(col: 0 ~ 3)
  for (int col = 0; col < 4; col++) {
    System.out.printf("* ");
  }
  // 줄 내림으로 행 구분
  System.out.println();
}
```

### 예제

주어진 코드는 행(R)과 열(C)의 정보를 입력받아 R x C의 별표시 행렬을 출력한다. 출력 예와 같은 결과를 얻도록 적절한 입력값을 넣으시오.

**입력 예**

행의 수 R, 열의 수 C라 할 때, `R C`의 형태로 입력

```
3 7
```

**출력 예**

```
* * * * * * * 
* * * * * * * 
* * * * * * * 
```

```java
public class Matrix {
  public static void main(String[] args) {
    // 입력값 받기
    int r = Integer.parseInt(args[0]); // 3
    int c = Integer.parseInt(args[1]); // 7
    
    // 매트릭스 출력
    printMatrix(r, c);
  }
  
  public static void printMatrix(int rowMax, int columnMax) {
    for (int i = 0; i < rowMax; i++) {
      for (int j = 0; j < columnMax; j++) {
        System.out.printf("* ");
      }
      System.out.println(); // 줄 개행
    }
  }
}
```

## 리뷰

### 예제

2단부터 9단까지, 구구단을 출력하는 프로그램을 작성하려 한다. 출력 예와 같은 결과를 얻도록, 코드를 완성하시오.

**출력 예**

```
2단
    2 x 1 = 2
    2 x 2 = 4
       ...
    2 x 9 = 18
...
9단
    9 x 1 = 9
       ...
    9 x 9 = 81
```

```java
// 자바 프로그램의 최소 단위! 클래스 생성!
public class GuGuDan {
  // 프로그램 실행의 시작점. 메인 메소드 작성
  public static void main(String[] args) {
    // 구구단 출력
    printGuGuDan();
  }
  
  public static void printGuGuDan() {
    /* 반복문을 사용하여 메소드를 완성하시오. */
    for (int i = 2 ; i <= 9; i++)
    printDan(i); // 2단 출력
  }
  
  public static void printDan(int dan) {
    System.out.printf("%d단\n", dan);
    // dan x 1, dan x 2, ... , dan x 9
    for (int j = 1; j <= 9; j++) {
      System.out.printf("\t"); // 들여쓰기
      System.out.printf("%d x %d = %d\n", dan, j, dan * j);
    }
  }
}
```

