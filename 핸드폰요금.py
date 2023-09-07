n = int(input()) # 통화의 개수
call_times = list(map(int,input().split())) # 공백으로 구분,

# 초기화
y_pay = 0
m_pay = 0

for i in range(n) :
    y_pay += (call_times[i] // 30) * 10 + 10 #통화 시간을 30으로 나눈 몫에 10을 더하면 해당 시간에 대한 요금이 계산됩니다.
    m_pay += (call_times[i] // 60) * 15 + 15

if y_pay > m_pay :
    print("M", m_pay) # 민식 요금이 더 저렴
elif y_pay < m_pay:
    print("Y", y_pay) # 영식 요금이 더 저렴
else:
    print("Y M", y_pay) # 요금이 같으면
