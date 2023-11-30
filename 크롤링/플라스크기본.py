from bs4 import BeautifulSoup
from flask import Flask, jsonify, Response, request
import requests
#위의 두줄 : 리액트의 액시오스와 같은 역할을 해줌
import json

app = Flask(__name__) # 진입지점

# 임의의 데이터, 실제 구현에서는 이 부분에 데이터베이스에서 가져온 데이터나
# 계산된 결과를 넣습니다.
data = {
    'stations' : ['강남역', '역삼역', '서울역'],
    'ridership' : [1000, 800, 1200]
}

# 기본적인 GET 요청을 처리하는 라우트
@app.route('/api/data', methods=['GET']) # 이게 호출되고 아래의 함수가 불려짐
def get_data():
    resp = Response(
        json.dumps(data, ensure_ascii=False), # ensure_ascii=False를 설정하여 JSON에 유니코드 문자 포함
        mimetype='application/json; charset=utf-8' # charset=utf-8을 명시적으로 설정
    )
    return resp

@app.route('/api/weather', methods=['GET'])
def get_weather():
    url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"

    # HTTP GET 요청
    resp = requests.get(url)

    # HTML 파싱
    soup = BeautifulSoup(resp.text, "html.parser")
    output = ""

    for loc in soup.select("location"): # 선택자에 로케이션
        output += f"<h3>{loc.select_one('city').string}<h3>"
        output += f"날씨 : {loc.select_one('wf').string}</br>"
        output += f"최저/최고 기온 : {loc.select_one('tmn')}/{loc.select_one('tmx')}</hr>"

    return output

#GET 요청시 쿼리파라미터 사용
@app.route('/api/query', methods=['GET'])
def get_query():
    output = ""
    item_type = request.args.get('type', default=None, type=None)
    item_color = request.args.get('color', default=None, type=None)
    output += f"<h1>{item_type}</h1>"
    output += f"<h1>{item_color}</h1>"
    return output

# 서버 실행
if __name__ == '__main__':
    app.run(debug=True) # 앱=플라스크, 진입지점이 맞으면 서버실행