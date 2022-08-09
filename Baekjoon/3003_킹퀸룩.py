import sys
input = sys.stdin.readline

black = [1, 1, 2, 2, 2, 8]
white = list(map(int, input().split())) # [0, 1, 2, 2, 2, 7] or [2 1 2 1 2 1]
for i in range(6):
    print(black[i] - white[i], end=' ')