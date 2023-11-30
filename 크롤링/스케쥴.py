import schedule
import time
import requests
from bs4 import BeautifulSoup

def perform_web_crawling():
    # 웹 크롤링 작업 수행하는 함수 만듦
    url = "http://www.naver.com"
    response = requests.get(url)
    if response.status_code == 200: # 성공이면
        soup = BeautifulSoup(response.text, "html.parser")
    print(soup)

def job():
    print("웹 크롤링을 수행합니다.")
    perform_web_crawling()

# 매일 정해진 시간에 동작하도록 구현
schedule.every().day.at("09:41").do(job)

while True:
    schedule.run_pending() # 1초마다 수행하고
    time.sleep(1) # 1초동안 자는 동안 스케쥴 돌림
