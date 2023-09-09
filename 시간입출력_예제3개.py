# 시, 분, 초
# 시간 형식 변환
hour, min, sec = map(int,input("시간 입력 : ").split(":"))
if hour > 12 :
    hour-=12
    print(f"오후{hour:02}시 {min:02}분 {sec:02}초")
else:
    print(f"오전{hour:02}시 {min:02}분 {sec:02}초")


# 요일 판별
import datetime

day_of_week = datetime.datetime.now().strftime("%A")
print("오늘은", day_of_week, "입니다.")


# 주말, 주중 판별
import datetime

current_date = datetime.datetime.now()
day_of_week = current_date.strftime("%A")

if day_of_week == "Saturday" or day_of_week == "Sunday":
    print("오늘은 주말입니다.")
else:
    print("오늘은 평일입니다.")
