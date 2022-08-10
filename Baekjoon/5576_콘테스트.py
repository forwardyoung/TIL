w = []
k = []

for i in range(20): # 총 20명
    if i < 10: # w 대학 10명 (인덱스 : 0~9)
        w.append(int(input()))
    else: # k 대학 10명 (인덱스 : 10~19)
        k.append(int(input()))
    # w 대학과 k 대학의 점수를 sort() 로 오름차순 정렬    
    w.sort() 
    k.sort()
# w 대학의 점수와 k 대학의 점수를 인덱스 7부터 끝까지 더한다. (득점이 높은 세 명)    
print(sum(w[7:]))
print(sum(k[7:]))