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

