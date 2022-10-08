# 프로그래머스 SQL 고득점 KIT 정리

> 🐾 2022.10.08 새로 업데이트 된 문제와 기존에 풀었던 문제 중 다시 풀어볼 만한, 헷갈리는 문제들 정리



## SELECT

- 동물 보호소에 들어온 모든 동물의 아이디와 이름, 보호 시작일을 이름 순으로 조회하는 SQL문

  ⚠️ 이름이 같은 동물 중에서는 **보호를 나중에 시작한 동물을 먼저** 보여줘야 한다.

```sql
SELECT ANIMAL_ID, NAME, DATETIME FROM ANIMAL_INS ORDER BY NAME, DATETIME DESC;
# 이름 순으로 조회 ORDER BY NAME
# 이름이 같다면 보호 시작일이 더 늦은 아이를 보여줘야 하므로 DATETIME 내림차순
```

- 동물 보호소에 들어온 동물 중 젊은 동물(`INTAKE_CONDITION`이 Aged가 아닌 경우를 뜻함)의 아이디와 이름을 조회하는 SQL 문.

  이때 결과는 **아이디 순**으로 조회

```sql
SELECT ANIMAL_ID, NAME FROM ANIMAL_INS WHERE INTAKE_CONDITION <> 'Aged' ORDER BY ANIMAL_ID;
# 조건은 WHERE절 사용
# 부정연산자 <>, !=
# 같다 =
```

- `MEMBER_PROFILE` 테이블에서 생일이 3월인 여성 회원의 ID, 이름, 성별, 생년월일을 조회하는 SQL문

  이때 전화번호가 NULL인 경우는 출력대상에서 제외, 결과는 **회원ID를 기준으로 오름차순 정렬**

  `DATE_OF_BIRTH` : 1992-02-22와 같은 형식

  ✔️ 3가지 조건

  1) 생일이 3월 ➡️ MONTH(DATE) : 지정된 날짜의 월 부분을 나타내는 정수를 반환
  2) 성별이 여성
  3) 전화번호 NULL이면 안 됨

```sql
SELECT MEMBER_ID, MEMBER_NAME, GENDER, DATE_OF_BIRTH FROM MEMBER_PROFILE
WHERE MONTH(DATE_OF_BIRTH) = 3 # 조건 1
AND GENDER = 'W' # 조건 2
AND TLNO IS NOT NULL # 조건 3
ORDER BY MEMBER_ID;
```

🔎 DAY(DATE) : 지정된 날짜의 일 부분을 나타내는 정수를 반환	

🔎 YEAR(DATE) : 지정된 날짜의 연도 부분을 나타내는 정수를 반환

- `FOOD_FACTORY` 테이블에서 **강원도에 위치**한 식품공장의 공장 ID, 공장 이름, 주소를 조회하는 SQL문

  이때 결과는 **공장 ID를 기준으로 오름차순 정렬**

  `ADDRESS` : 강원도 정선군 남면 칠현로 679와 같은 형식

```sql
SELECT FACTORY_ID, FACTORY_NAME, ADDRESS FROM FOOD_FACTORY WHERE ADDRESS LIKE '강원도%' ORDER BY FACTORY_ID;
# 강원도에 위치한 식품공장은 ADDRESS가 '강원도'로 시작 혹은 '강원도'를 포함해야 한다. LIKE '강원도%' 또는 LIKE '%강원도%'
```

- `REST_INFO`와 `REST_REVIEW` 테이블에서 서울에 위치한 식당들의 식당 ID, 식당 이름, 음식 종류, 즐겨찾기수, 주소, 리뷰 평균 점수를 조회하는 SQL문

  이때 **리뷰 평균점수는 소수점 세 번째 자리에서 반올림**, **결과는 평균점수를 기준으로 내림차순 정렬**, **평균점수가 같다면 즐겨찾기수를 기준으로 내림차순 정렬**

`REST_INFO` 테이블

| REST_ID | REST_NAME    | FOOD_TYPE | VIEWS  | FAVORITES | PARKING_LOT | ADDRESS                                  | TEL          |
| ------- | ------------ | --------- | ------ | --------- | ----------- | ---------------------------------------- | ------------ |
| 00028   | 대우부대찌개 | 한식      | 52310  | 10        | N           | 경기도 용인시 처인구 남사읍 처인성로 309 | 031-235-1235 |
| 00039   | 광주식당     | 한식      | 23001  | 20        | N           | 경기도 부천시 산업로8번길 60             | 031-235-6423 |
| 00035   | 삼촌식당     | 일식      | 532123 | 80        | N           | 서울특별시 강서구 가로공원로76가길       | 02-135-1266  |

`REST_REVIEW` 테이블

| EVIEW_ID   | REST_ID | MEMBER_ID             | REVIEW_SCORE | REVIEW_TEXT                          | REVIEW_DATE |
| ---------- | ------- | --------------------- | ------------ | ------------------------------------ | ----------- |
| R000000065 | 00028   | `soobin97@naver.com`  | 5            | 부찌 국물에서 샤브샤브 맛이나고 깔끔 | 2022-04-12  |
| R000000066 | 00039   | `yelin1130@gmail.com` | 5            | 김치찌개 최곱니다.                   | 2022-02-12  |
| R000000067 | 00028   | `yelin1130@gmail.com` | 5            | 햄이 많아서 좋아요                   | 2022-02-22  |
| R000000068 | 00035   | `ksyi0316@gmail.com`  | 5            | 숙성회가 끝내줍니다.                 | 2022-02-15  |
| R000000069 | 00035   | `yoonsy95@naver.com`  | 4            | 비린내가 전혀없어요.                 | 2022-04-16  |

SQL을 실행하면 다음과 같이 출력돼야 한다.

| REST_ID | REST_NAME | FOOD_TYPE | FAVORITES | ADDRESS                            | SCORE |
| ------- | --------- | --------- | --------- | ---------------------------------- | ----- |
| 00035   | 삼촌식당  | 일식      | 80        | 서울특별시 강서구 가로공원로76가길 | 4.50  |