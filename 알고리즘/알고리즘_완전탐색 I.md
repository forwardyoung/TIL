# 완전탐색 I (Exhaustive Search)

> ## 1. 무식하게 다해보기 (Brute-force)
>
> : 모든 경우의 수를 탐색하여 문제를 해결하는 방식

- 브루트포스라고도 하며, 무식하게 밀어붙인다는 뜻
- 가장 단순한 풀이 기법이며, 단순 조건문과 반복문을 이용해서 풀 수 있다.
- 복잡한 알고리즘보다는, 아이디어를 어떻게 코드로 구현할 것인지가 중요하다.

📍 블랙잭 문제를 통해 완전탐색 이해하기 - [BOJ 2798](https://www.acmicpc.net/problem/2798) (knapsack problem)

예제 입력 1)

5장의 카드 5, 6, 7, 8, 9 중 세 장의 카드의 합(max_total)이 21이 넘지 않아야 한다.

```python
for i in range(5):
    for j in range(5):
        for k in range(5):
# 반복문이 총 125번 순회

for i in range(3):
    # 0, 1, 2
    for j in range(i+1, 4):
		# 1, 2, 3
        for k in range(j+1, 5):
            # 2, 3, 4
# 위의 코드보다 반복문이 순회하는 횟수가 적다.

# 두 코드는 '시간 복잡도 관점'에서는 동일하다! --> O(n^3)
```



```python
def blackjack(n, m, cards):
    max_total = 0 # 현재 가장 큰 합
    
    # 완전탐색(Brute-force)
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                total = cards[i] + cards[j] + cards[k]
                
                # 현재 가장 큰 합보다는 크고, m을 넘지 않아야 갱신
                if max_total<total<=m:
                    max_total = total
                # 합과 m이 같으면 더 이상 탐색하는 의미가 없으므로 종료
                if total == m :
                    return total
         
return max_total        
```





> ## 2. 델타 탐색 (Delta Search)
>
> : (0, 0)에서부터 이차원 리스트의 모든 원소를 순회하며(완전탐색) **각 지점에서 상하좌우에 위치한 다른 지점을 조회하거나 이동**하는 방식

이차원 리스트의 인덱스(좌표)의 조작을 통해서 상하좌우 탐색을 한다.

이때 행과 열의 변량인 -1, +1을 **델타(delta)값**이라 한다.

![델타 탐색](https://github.com/forwardyoung/TIL/blob/master/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98_Brute-force%20%26%20Delta%20Search.assets/%EB%8D%B8%ED%83%80%20%ED%83%90%EC%83%89.png)

1️⃣ 델타값 정의(상하좌우)

```python
# 행을 x, 열을 y로 표현 (행을 r, 열을 c로 표현하기도 함)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
== > [상, 하, 좌, 우]
```

![델타값 정의](https://github.com/forwardyoung/TIL/blob/master/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98_Brute-force%20%26%20Delta%20Search.assets/%EB%8D%B8%ED%83%80%EA%B0%92%20%EC%A0%95%EC%9D%98.png)

2️⃣ 이차원 리스트 순회 및 델타값을 이용해 상하좌우 이동

```python
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# (1, 1)

for i in range(4):
    for j in range(4):
        # i, j => 0, 0 ~ 3, 3
        # i, j => 1, 1
        for d in delta:
            print(i + d[0], j + d[1])
```

```python
# 상(x-1, y)
nx = x + dx[0]
ny = y + dy[0]

# 하(x+1, y)
nx = x + dx[1]
ny = y + dy[1]

# 좌(x, y-1)
nx = x + dx[2]
ny = y + dy[2]

# 우(x, y+1)
nx = x + dx[3]
ny = y + dy[3]

# 상하좌우
for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
```

3️⃣ 범위를 벗어나지 않으면 갱신

⚠️ 상하좌우로 이동 후 범위를 벗어나지 않는지 확인 및 갱신하기

![범위 확인](https://github.com/forwardyoung/TIL/blob/master/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98_Brute-force%20%26%20Delta%20Search.assets/%EB%B2%94%EC%9C%84%20%ED%99%95%EC%9D%B8.png)

```python
# 1. 델타값을 이용해 상하좌우 이동
for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    
    # 2. 범위를 벗어나지 않으면 갱신
    if 0 <= nx < 3 and 0<= ny < 3:
        x = nx
        y = ny
```

📍 **상하좌우 + 대각선**의 8방향 델타값

![8방향 델타값](https://github.com/forwardyoung/TIL/blob/master/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98_Brute-force%20%26%20Delta%20Search.assets/8%EB%B0%A9%ED%96%A5%20%EB%8D%B8%ED%83%80%EA%B0%92.png)
