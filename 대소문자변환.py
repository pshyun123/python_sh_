# 입력 받기
word = input()

# 대문자를 소문자로, 소문자를 대문자로
result = '' #빈문자열 생성, 결과 저장 준비
for char in word:
    if char.isupper(): #입력받은 단어를 한 글자씩 순회.대문자인지 소문자인지 확인
        result += char.lower()
    else:
        result += char.upper()

print(result)

