import sys
input = sys.stdin.readline
# 숫자 5를 볼 때, 5로 볼 때도 있지만, 6으로 잘못 볼 수도 있고,
# 6을 볼 때는, 6으로 볼 때도 있지만, 5로 잘못 볼 수도 있다.
# 입력 받은 두 수의 합 중 최솟값과 최댓값을 출력한다.
a, b = input().split()
min = int(a.replace('6', '5')) + int(b.replace('6', '5')) # 6을 5로 바꾸면 6을 6으로 보는 것보다 작아질 것임
max = int(a.replace('5', '6')) + int(b.replace('5', '6')) # 5를 6으로 바꾸면 5를 5로 보는 것보다 커질 것임
print(min, max)