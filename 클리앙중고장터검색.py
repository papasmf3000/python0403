# coding:utf-8
from bs4 import BeautifulSoup
#웹서버에 요청(통신)
import urllib.request
#특정한 주제를 필터링
import re 

#웹봇으로 크롤링을 금지
#User-Agent를 조작하는 경우(아이폰에서 사용하는 사파리 브라우져의 헤더) 
hdr = {'User-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/603.1.23 (KHTML, like Gecko) Version/10.0 Mobile/14E5239e Safari/602.1'}

for n in range(0,10):
        #클리앙의 중고장터 주소 
        data ='https://www.clien.net/service/board/sold?&od=T31&po=' + str(n)
        print(data)
        #웹브라우져 헤더 추가 
        req = urllib.request.Request(data, headers = hdr)
        data = urllib.request.urlopen(req).read()
        #한글이 깨지는 경우는 유니코드로 다시 해석 
        page = data.decode('utf-8', 'ignore')
        soup = BeautifulSoup(page, 'html.parser')
        list = soup.find_all('span', attrs={'data-role':'list-title-text'})
        # <span class="subject_fixed" data-role="list-title-text" title="아이패드 에어3 10.5인치 64GB LTE+Wi-Fi 팝니다.">
        # 	아이패드 에어3 10.5인치 64GB LTE+Wi-Fi 팝니다.
        # </span>
        for item in list:
                try:
                        title = item.text  
                        print(title.strip())
                        # if (re.search('아이폰', title)):
                        #         print(title.strip())
                except:
                        pass
        
