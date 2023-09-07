
# A, B, C 입력 받기
A,B,C = map(int, input("정수 3개 입력 : ").split())

# A * B * C 계산
result = str(A * B * C)
# 결과를 문자열로 변환하여 각 숫자의 등장 횟수를 세기 쉽게 처리

# # 0부터 9까지의 숫자가 등장한 횟수를 저장할 리스트 초기화
# count = [0] * 10
#
# # 숫자 등장 횟수 계산
# for d in result:
#     count[int(d)] += 1
#
# # 결과 출력
# for i in range(10):
#     print(count[i])

for i in range(10):
    print(result.count(str(i)))