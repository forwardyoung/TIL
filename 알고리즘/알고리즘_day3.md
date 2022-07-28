# 문자열(String)

⚠️ 문자열은 immutable(변경 불가능한) 자료형!



## 1. 문자열 슬라이싱

s = 'abcdefghi'

🍯 방향부터 확인한다!

- s[2:5:2] : 'ce'

- s[-6:1:3] : 'dg'

- s[5:2]  : ❓

  🍯 비행기 표 예약할 때를 생각하면 가는 날짜가 돌아오는 날짜보다 클 수 없다! 

- s[2:5:-1] : ❓

  - [::]에서 마지막 인자는 몇 개를 skip할 것인지를 의미
  - 마지막 인자에 '-'가 들어가는 순간 인덱스를 세는 방향이 반대

- s[5:2:-1] : 'fed'																					

​																					🔙												

|       | a    | b    | c    | d    | e    | f    | g    | h    | i    |
| :---: | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| index | 0    | 1    | 2    | 3    | 4    | 5    | 6    | 7    | 8    |
| index | -9   | -8   | -7   | -6   | -5   | -4   | -3   | -2   | -1   |

🍯 음의 인덱스 + 문자열의 길이 = 양의 인덱스

ex) 'd'의 음의 인덱스 (-6) + 9 = 'd'의 양의 인덱스 (3)

**[풀어보기](https://www.acmicpc.net/problem/10988)** : BOJ 10988 팰린드롬인지 확인하기



## 2. 문자열 메서드

⚠️ time complexity를 고려하고 사용한다. 대부분 O(n)

1️⃣ **.split(기준 문자)**

- 문자열을 일정 **기준**으로 나누어 **리스트로 반환**

- 괄호 안에 아무것도 넣지 않으면 자동으로 공백을 기준으로 설정

```python
word = "This_is_snake_case"
print(word.split("_"))
# ['This', 'is', 'snake', 'case']
```

2️⃣ **.strip(제거할 문자)**

- 문자열의 **양쪽** 끝에 있는 특정 문자를 모두 **제거**한 새로운 문자열 반환
- 괄호 안에 아무것도 넣지 않으면 자동으로 공백을 제거 문자로 설정
- 제거할 문자를 여러 개 넣으면 해당하는 모든 문자들을 제거

⚠️ **원본은 변하지 않는다 -- imutable**

```python
word = "Hello World"
print(word.strip("Hd"))
# ello Worl
```

3️⃣ **.find(찾는 문자)**

- 특정 문자가 처음으로 나타나는 **위치(인덱스)**를 반환
- 찾는 문자가 없다면 **-1**을 반환

```python
word = "apple"
print(word.find("k"))
# -1
```

4️⃣ **.index(찾는 문자)**

- 특정 문자가 처음으로 나타나는 **위치(인덱스)**를 반환

- 찾는 문자가 없다면 **오류** 발생 -- 실행이 끝남

```python
word = "apple"
print(word.index("k"))
----------------------
ValueError
Input ln [21], in <cell lir
	  1 word = "apple"
-----> 3 print(word.index("k"))
ValueError : substring not
```

5️⃣ **.count(개수를 셀 문자)**

- 문자열에서 특정 문자가 **몇 개**인지 반환
- 문자 뿐만 아니라, 문자열의 개수도 확인 가능

```python
word = "banana"
print(word.count("na"))
# 2
```

6️⃣ **.replace(기존 문자, 새로운 문자)**

- 문자열에서 기존 문자를 새로운 문자로 **수정**한 새로운 문자열 반환
- 특정 문자를 빈 문자열("")로 수정하여 마치 해당 문자를 삭제한 것 같은 효과 가능

```python
word = "happyhacking"
print(word.replace("happy", ""))
# hacking
```

7️⃣ **삽입할문자.join*(iterable)***

- *iterable*의 **각각 원소 사이에 특정 문자를 삽입**한 새로운 문자열 반환
- 공백 출력, 콤마 출력 등 원하는 **출력** 형태를 위해 사용

```python
word = ["edu", "hphk.kr"]
print("@".join(word))
# edu@hphk.kr

word = "happyhacking"
print(" ".join(word))
# h a p p y h a c k i n g
```

**[풀어보기](https://www.acmicpc.net/problem/17249)** : BOJ 17249 태보태보 총난타



## 3. 아스키(ASCII) 코드

📍 **컴퓨터는 숫자만 이해할 수 있다!**

|         비트(bit)         |        바이트(byte)         |
| :-----------------------: | :-------------------------: |
| 0과 1 두 가지 정보만 표현 | 데이터를 저장하는 기본 단위 |

📍 **그렇다면 문자는 어떻게 저장될까?**

➡️ **ASCII** (American Standard Code for Information Interchange) : 미국 정보교환 표준부호

📍 **아스키(ASCII) 코드란?**

: 알파벳을 표현하는 대표 인코딩 방식

각 문자를 표현하는 데 1byte(8bits) 사용

- 1 bit : 통신 에러 검출용
- 7 bit : 문자 정보 저장 (총 128개)

(1) **ord(문자)** : **문자 ➡️ 아스키코드**로 변환하는 내장함수

```python
print(ord("A"))
# 65
print(ord("a"))
# 97
```

(2) **chr(아스키코드)** : **아스키코드 ➡️ 문자**로 변환하는 내장함수

```python
print(chr(65))
# A
print(chr(97))
# a
```

**[풀어보기](https://www.acmicpc.net/problem/10809)** : BOJ 10809 알파벳 찾기

