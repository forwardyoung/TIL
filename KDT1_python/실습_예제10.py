# 아래 코드는 리스트에서 최댓값을 구하는 코드입니다.
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.

number_list = [1, 23, 9, 6, 91, 59, 29]
# max = max(number_list) -- TypeError: 'int' object is not callable ; 예약어(max(), min(), sum() 등)을 변수명으로 사용할 때 발생하는 오류
# 변수명을 max가 아닌 다른 것으로 바꾼다!
a = max(number_list)

number_list2 = [2, 5, 100, 20, 50, 10, 91, 82]
b = max(number_list2)

if a > b:
    print("첫 번째 리스트의 최댓값이 더 큽니다.")

elif a < b:
    print("두 번째 리스트의 최댓값이 더 큽니다.")

else:
    print("첫 번째 리스트의 최댓값과 두 번째 리스트의 최댓값은 같습니다.")