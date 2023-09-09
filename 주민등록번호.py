import datetime
current_year = datetime.datetime.today().year

j = input("주민번호 : ")
gender = int(j[7])
year = int(j[:2])
month = int(j[2:4])
day = int(j[4:6])

if gender == 1 or gender == 2:
    age = current_year - 1900 - year  # 2023-1900-95
else:
    age = current_year - 2000 - year

if gender == 1 or gender == 3:
    gender_str = "남성"
else:
    gender_str = "여성"

print(f"생년월일 : {year}년 {month}월 {day}일")
print(f"성별 : {gender_str}입니다.")
print(f"나이 : {age}입니다.")

# 방법 2
from datetime import datetime

jumin = input("주민등록번호 : ")
gender = "남성" if int(jumin[7]) in (1, 3) else "여성"
year = int(jumin[:2])
year += 1900 if year < 22 else 2000
month, day = int(jumin[2:4]), int(jumin[4:6])
current_year = datetime.today().year
age = current_year - year

print(f"생년월일: {year}년 {month}월 {day}일")
print(f"성별: {gender}")
print(f"나이: {age}세")