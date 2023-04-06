# coding:utf-8
from bs4 import BeautifulSoup
#웹서버에 요청(통신)
import urllib.request
#특정한 주제를 필터링
import re 

#웹봇으로 크롤링을 금지
#User-Agent를 조작하는 경우(아이폰에서 사용하는 사파리 브라우져의 헤더) 
hdr = {'User-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/603.1.23 (KHTML, like Gecko) Version/10.0 Mobile/14E5239e Safari/602.1'}

#파일에 저장(r: raw string notation)
#기존 컨텐츠에 추가(append, read, write: a+)
f = open(r"c:\work\todayHumor.txt", "a+", encoding="utf-8")
#현재는 1~10페이지
for n in range(1,11):
        #클리앙의 중고장터 주소 
        data = 'https://www.todayhumor.co.kr/board/list.php?table=bestofbest&page=' + str(n)
        print(data)
        #웹브라우져 헤더 추가 
        req = urllib.request.Request(data, headers = hdr)
        data = urllib.request.urlopen(req).read()
        #한글이 깨지는 경우는 유니코드로 다시 해석 
        page = data.decode('utf-8', 'ignore')
        soup = BeautifulSoup(page, 'html.parser')
        list = soup.find_all('td', attrs={'class':'subject'})
        #<td class="subject">
        # <a href="/board/view.php?table=bestofbest>우리를 악에서 
        for item in list:
                try:
                        title = item.find('a').text.strip()  
                        #print(title)
                        if (re.search('한국', title)):
                                print(title.strip())
                                f.write(title.strip() + "\n")
                except:
                        pass
        

f.close() 