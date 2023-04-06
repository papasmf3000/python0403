# DemoForm2.py 
# DemoForm2.ui(화면단) + DemoForm2.py(로직단)
import sys 
from PyQt5.QtWidgets import * 
from PyQt5 import uic 
#웹서버에 요청
import requests
#크롤링
from bs4 import BeautifulSoup


#화면을 로딩
form_class = uic.loadUiType("DemoForm2.ui")[0]
#윈도우(폼)클래스 정의(QMainWindow)
class DemoForm(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    #슬롯메서드 추가
    def firstClick(self):
        url = "https://www.daangn.com/"
        response = requests.get(url)
        #검색이 용이한 객체 생성
        soup = BeautifulSoup(response.text, "html.parser")

        posts = soup.find_all("div", attrs={"class":"card-desc"})
        for post in posts:
            title = post.find("h2", attrs={"class":"card-title"})
            price = post.find("div", attrs={"class":"card-price"})
            addr = post.find("div", attrs={"class":"card-region-name"})
            print("{0} , {1} , {2}".format(title, price, addr))
        self.label.setText("당근 크롤링 완료~~")
    def secondClick(self):
        self.label.setText("두번째 버튼입니다~~")
    def thirdClick(self):
        self.label.setText("여기는 세번째~~")

#직접 이 모듈을 실행한 경우체크 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoForm = DemoForm() 
    demoForm.show() 
    app.exec_()
