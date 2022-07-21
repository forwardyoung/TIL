import sys
sys.stdin = open("input_1545.txt", "r")

n = int(input())
# 풀이 1
for i in range(n, -1, -1):
    print(i,end=' ')
# for i in range(n, 0, -1): 결과값이 8~1 출력된다.
# range(start, stop, step)

# 풀이 2
for i in reversed(range(n+1)):
    print(i,end =' ')