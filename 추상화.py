# 추상화 :
# 부모 클래스에서 선언한 메소드를 반드시 상속 받은 클래스에서 기능을 구현 해야함
# 추상 메서드가 포함된 부모 클래스는 객체로 X, 상속 주기 위해서만 존재함

from abc import *
class NetworkAdapter(metaclass=ABCMeta): # 추상클래스 선언
    @abstractmethod         # 추상메소드를 어노테이션
    def connect(self): pass # 추상화하려면 구현부가 없어야 함. 그래서 패스

class WiFi(NetworkAdapter) :
    def __init__(self, company): # 생성자 만들기
        self.company = company
    def connect(self): # 부모에게서 상속받은 추상메서드 구현함(필수)
        print(f"{self.company} Wi-Fi에 연결 했습니다.")

class FiveG(NetworkAdapter) :
    def __init__(self, company): # 생성자 만들기
        self.company = company
    def connect(self): # 부모에게서 상속받은 추상메서드 구현함(필수)
        print(f"{self.company} 5G에 연결 했습니다.")
net = input("연결할 네트워크 선택 : [1]WiFi [2]5G :")
if net == "1":
    adapter = WiFi("KT megapass")
    adapter.connect()
elif net == "2" :
    adapter = FiveG("LG U+")
    adapter.connect()
else: print("연결할 네트워크가 없습니다.")