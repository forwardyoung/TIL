n, m = map(int, input().split())
for i in range(1, n+1) : # i 값이 1~n까지 바뀌는 동안
  for j in range(1, m+1) : # j 값이 1~n까지 변하며 출력
    print(i, j)