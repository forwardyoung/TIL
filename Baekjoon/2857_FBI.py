import sys
sys.stdin = open("2857.txt")

n = 5
list_ = []
for _ in range(5):
    members = input()
    list_.append(members)
# print(list_)
cnt = 0
for i in range(5):
    if 'FBI' in list_[i]:
        print(i+1)
        cnt += 1
if cnt == 0:
    print('HE GOT AWAY!')