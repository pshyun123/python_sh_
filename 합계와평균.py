
#4. 개수가 정해지지 않은 여러 개의 정수를 입력 받아 합계와 평균 구하기

score = list(map(int, input("정수 : ").split()))
print(f"총점 : {sum(score)}")
print(f"평균 : {sum(score)/len(score)}") # 갯수만큼 나눠줌