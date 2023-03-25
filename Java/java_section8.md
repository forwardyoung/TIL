# 배열

> type의 일종으로, 여러 데이터를 하나로 묶는 방법

```java
// 배열 생성
int[] students = { 65, 74, 23, 75, 68, 96, 88, 98, 54 };

// 반복문 작성
for ( int i = 0; i < 10; i++) {
    System.out.println("학생-%d :%d점\n", i, students[i]);
}

/* 
학생-0 : 65점
학생-1 : 74점
...
학생-8 : 54점
... */
```

![image-20230325162007401](C:\Users\726jo\AppData\Roaming\Typora\typora-user-images\image-20230325162007401.png)

- 모두 같은 타입이다.

```java
/// int 배열
int[] students = { 65, 74, 23, 75, 68, 96, 88, 98, 54 };

// double 배열
double[] students = { 2.8, 3.5, 4.2, 4.5, 3.2};
```

## 배열의 생성과 사용

**생성**

1️⃣ 생성과 동시에 초기화

중괄호에 값들을 넣어 만든다. 이때, 타입 뒤쪽에 대괄호(`[]`)가 필요

```java
// int 배열 scores를 생성
int[] scores = { 90, 68, 77, 98 };
// String 배열 names를 생성
String[] names = {"Sam", "Kate", "John", "Jeny"};
```

2️⃣ 공간 할당 후 값 대입

크기를 먼저 잡고 하나씩 대입하는 방식

```java
// 1 먼저 배열의 크기 설정 후,
int[] arr = new int[4];
// 2 인덱스별 값 대입
arr[0] = 11;
arr[1] = 22;
arr[2] = 33;
arr[4] = 44;
```

**사용**

배열에 담긴 값들은, 인덱스(index)라는 위치를 통해 접근 가능

```java
System.out.println(names[0]); // "Sam"
System.out.println(names[1]); // "Kate"
System.out.println(names[2]); // "John"
System.out.println(names[3]); // "Jeny"
```

```java
// 1) 배열 값 읽기(read)
int[] scores = {99, 88, 77};
System.out.println(scores[0]); // 99
System.out.println(scores[1]); // 88
System.out.println(scores[2]); // 77
// 2) 배열 값 변경(write)
System.out.println(scores[0]); // 99
scores[0] = 0; // 0번 인덱스 값 변경
System.out.println(scores[0]); // 0
```

### 예제

1. 대학교를 갓 졸업한 나컴공 학생의 학점은 아래와 같다.

- 1학년: 3.45
- 2학년: 2.82
- 3학년: 3.85
- 4학년: 3.94

위 학점에 대한 정보를 배열로 생성하고, 출력 예와 같은 결과를 얻으시오.

**출력 예**

```
1학년: 3.45
2학년: 2.82
3학년: 3.85
4학년: 3.94
```

```java
public class Grade {
  public static void main(String[] args) {
    // 배열 생성
    double[] grades = { 3.45, 2.82, 3.85, 3.94};
    
    /* 2. 적절한 출력을 만드시오. */
    System.out.printf("1학년: %.2f\n", grades[0]);
    System.out.printf("2학년: %.2f\n", grades[1]);
    System.out.printf("3학년: %.2f\n", grades[2]);
    System.out.printf("4학년: %.2f\n", grades[3]);
  }
}
```

2. 이번 한 주간 아메리카노의 판매량은 아래와 같다.

- 월: 52 잔

- 화: 50 잔

- 수: 55 잔

- 목: 42 잔

- 금: 38 잔

배열을 사용하여 아메리카노의 판매량을 저장하고 이에 대한 총합을 구하시오.

**출력 예**

```
총 판매량: 237잔
```

```java
public class Americano {
  public static void main(String[] args) {
    // 배열 생성
    int[] sales = new int[5]; // 배열의 크기 지정
    
    // 배열 값 초기화
    sales[0] = 52; // 월
    sales[1] = 50; // 화
    sales[2] = 55; // 수
    sales[3] = 42; // 목
    sales[4] = 38; // 금
    
    // 배열 합 계산
    int sum = sales[0] + sales[1] + sales[2] + sales[3] + sales[4];
    
    // 출력
    System.out.printf("총 판매량: %d잔\n", sum);
  }
}
```

## 반복문

- 배열 요소들의 총합을 구할 수 있다.

```java
# 변수 생성
int[] scores = { 88, 76, 92, 68, 55, 48, 82 };
int sum = 0;
# 배열 요소의 합 계산
for (int i = 0; i < 7; i++) {
  sum += scores[i];
}
# 출력
System.out.println(sum); // 509
```

### 예제

홍팍이는 건강을 위해 조깅을 시작했다. 그 한 주간 달리기 기록이 아래와 같을 때, 달리기 시간의 총합과 평균을 출력 예와 같이 얻으시오.

- 월: 42분
- 화: 66분
- 수: 57분
- 목: 54분
- 금: 88분

**출력 예**

```
달리기 시간 총합: 307분
달리기 시간 평균: 61분
```

```java
public class SumArray {
 public static void main(String[] args) {
    // 변수 생성
    int[] runningMinutes = { 42, 66, 57, 54, 88 };
    int sum = 0;

    /* 하나씩 더하는 방법
    sum += runningMinutes[0];
    sum += runningMinutes[1];
    sum += runningMinutes[2];
    sum += runningMinutes[3];
    sum += runningMinutes[4];
     */
    /* for문으로 총합을 구하는 방법 */
    for ( int i = 0; i < 5; i++) {
      sum += runningMinutes[i];
    }
    
    /* 2. 평균을 계산하시오. */
    double average = sum / 5.0;

    // 결과 출력
    System.out.printf("달리기 시간 총합: %d분\n", sum);
    System.out.printf("달리기 시간 평균: %.0f분\n", average);
  }
}
```

## 배열의 길이

- `length` 키워드를 사용하여 구할 수 있다.

```java
// 배열 생성
String[] courses = { "자바", "자료구조", "알고리즘" };

// 배열의 길이 출력
System.out.println(courses.length); // 3
```

- length 키워드는 모든 배열 순회 시 사용 가능하다.

```java
// 기존 방법
for (int i = 0; i < 3; i++) {
  System.out.println("%s\n", courses[i]);
}

// length 활용법
for (int i = 0; i < courses.length; i++) {
  System.out.println("%s\n", courses[i]);
}
```

### 예제

CS대학의 과정들은 핵심(cores), 선택(electives), 교양(general) 과목으로 나뉘며 각 내용은 아래와 같다.

|      분류       | 과정명                                     |
| :-------------: | :----------------------------------------- |
|   핵심(cores)   | 자바, 자료구조, 알고리즘, 데이터베이스     |
| 선택(electives) | 컴퓨터 네트워크, 운영체제, 소프트웨어 공학 |
| 교양(generals)  | 영어회화, 영독해, 영작문, 팀워크, 직업윤리 |

이들을 출력하기 위해 주어진 코드는 위 정보들을 배열화하고있다. 출력 예와 같은 결과를 얻도록 코드를 완성하시오.

**출력 예**

```
핵심과정: 자바 자료구조 알고리즘 데이터베이스 
선택과정: 컴퓨터 네트워크 운영체제 소프트웨어 공학 
교양과정: 영어회화 영독해 영작문 팀워크 직업윤리 
```

```java
public class ArrayLength {
  public static void main(String[] args) {
    // 변수 생성
    String[] cores = {"자바", "자료구조", "알고리즘", "데이터베이스"};
    String[] electives = {"컴퓨터 네트워크", "운영체제", "소프트웨어 공학"};
    String[] generals = {"영어회화", "영독해", "영작문", "팀워크", "직업윤리"};
    
    // 핵심 과정 출력
    System.out.printf("핵심과정: ");
    for (int i = 0; i < cores.length; i++) {
      System.out.printf("%s ", cores[i]);
    }
    
    // 선택 과정 출력
    System.out.printf("\n선택과정: ");
    for (int i = 0; i < electives.length; i++) {
      System.out.printf("%s ", electives[i]);
    }
    
    // 교양 과정 출력 //
    System.out.printf("\n교양과정: ");
    for (int i =0; i < generals.length; i++) {
      System.out.printf("%s ", generals[i]);
    }
  }
}
```

## 벗어난 인덱스

- 길이가 N인 배열의 인덱스는 **0**부터 시작하고, 그 끝은 `N-1`이 된다. 배열의 인덱스를 넘어가면 에러가 발생한다.

> Exception in thread "main" java.lang.ArrayIndexOutOfBoundsException: -1
>
> ​	at OutOfIndex.main(OutOfIndex.java:7)

```java
// 정수형 배열
int[] scores = { 88, 72, 96, 28, 60 };
// 에러 발생
scores[-5] = 0; // (X)
scores[100] = 5; // (X)
```

### 예제

주어진 코드의 에러 원인을 찾고, 이를 수정하여 출력 예와 같은 결과를 얻으시오.

**출력 예**

```
names[-1] => 에러!! 인덱스는 음수가 될 수 없음.
names[0] => Kim
names[1] => Lee
names[2] => Park
names[3] => Choi
names[4] => 에러!! 배열 인덱스를 벗어남.
```

```java
public class OutOfIndex {
  public static void main (String[] args) {
    // 배열 생성
    String[] names = { "Kim", "Lee", "Park", "Choi" };
    
    // 배열요소 출력
    System.out.printf("names[%d] => %s\n", -1, "에러!! 인덱스는 음수가 될 수 없음.");
    System.out.printf("names[%d] => %s\n", 0, names[0]);
    System.out.printf("names[%d] => %s\n", 1, names[1]);
    System.out.printf("names[%d] => %s\n", 2, names[2]);
    System.out.printf("names[%d] => %s\n", 3, names[3]);
    System.out.printf("names[%d] => %s\n", 4, "에러!! 배열 인덱스를 벗어남.");
  }
}
```

## 배열과 파라미터

**변수를 메소드로 전달**

```java
// 변수 생성
double a = 10.4;
double b = 6.6;
double result = add(a, b);
```

**배열을 메소드로 전달**

```java
# 배열 생성
int[] numbers = { 1, 3, 1, 8 };
# 메소드 호출
int result = average(numbers);
```

- 배열을 전달받기 위해선, 파라미터의 타입 또한 배열로 선언해야 한다.

```java
# 메소드 정의부
public static int average(int[] arr) {
  ...
}
```

### 예제

0 이상 20 미만의 정수 중, 짝수와 소수의 합을 구하려 한다. (소수란 1과 자기 자신만으로 나누어떨어지는 1보다 큰 양의 정수)

출력 예와 같은 결과를 얻도록, sum() 메소드를 완성하시오.

**출력 예**

```
0 이상 20 미만의 짝수와 소수 중..
짝수의 합: 90
소수의 합: 77
```

```java
public class ArrayToParameter {
  public static void main(String[] args) {
    // 배열 생성
    int[] evens = { 0, 2, 4, 6, 8, 10, 12, 14, 16, 18 }; // 짝수
    int[] primes = { 2, 3, 5, 7, 11, 13, 17, 19 }; // 소수
    
    // 계산
    int evenSum = sum(evens);
    int primeSum = sum(primes);
    
    // 출력
    System.out.println("0 이상 20 미만의 짝수와 소수 중..");
    System.out.printf("짝수의 합: %d\n", evenSum);
    System.out.printf("소수의 합: %d\n", primeSum);
  }

  // 정수형 배열을 입력 받아 총합을 반환
  public static int sum(int[] arr) {
    int sum = 0;
    // 반복문을 통한 총합 계산
    for (int i = 0; i < arr.length; i++) {
      sum += arr[i];
    }
    return sum;
  }
}
```

## 배열의 평균값

### 예제

이번 한 주간 클라우드스터딩에 접속한 사용자 수는 아래와 같다.

- 월: 581명
- 화: 512명
- 수: 527명
- 목: 495명
- 금: 423명
- 토: 141명
- 일: 236명

하루 평균 접속자를 출력 예와 같이 구하도록 average() 메소드를 완성하시오.

**출력 예**

```
하루 평균 사용자: 416.43명
```

```java
public class DailyUser {
  public static void main(String[] args) {
    // 배열 생성
    int[] users = { 581, 512, 527, 495, 423, 141, 236 };
    
    // 계산
    double dailyUser = average(users);
    
    // 출력
    System.out.printf("하루 평균 사용자: %.2f명", dailyUser);
  }

  // 정수 배열을 입력받아, 평균을 반환
  public static double average(int[] arr) {
    // 1. 총합을 구하시오.
    double sum = 0;
    for (int i = 0; i < arr.length; i++) {
      sum += arr[i];
    }
    
    // 2. 평균을 계산하시오.
    double avg = sum / arr.length;

    // 결과값 반환
    return avg;
  }
}
```

