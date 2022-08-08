month = int(input())
if month == 12 or month == 1 or month == 2:
    print('winter')
    # 9 -- 6 -- 3 순서 주의!
elif month//9 == 1: # '//' 몫을 정수값으로
    print('fall')
elif month//6 == 1:
    print('summer')
elif month//3 == 1: 
    print('spring')
