import requests
import json

#JSON 데이터 생성
data = {
    "id":"짱구",
    "pwd":"thgus1204"
}

#  JSON 데이터 서버로 전달하기
url = "http://localhost:8111/test/python"
headers = {"Content-Type" : "application/json"}
resp = requests.post(url, data=json.dumps(data), headers=headers)#json 형태의 데이터 만들어 날려줌

# 서버 응답 확인
if resp.status_code == 200:
    print("데이터가 성공적으로 전송되었습니다.")
else:
    print("데이터 전송에 실패했습니다.", resp.status_code)