# web1.py 
#크롤링 
from bs4 import BeautifulSoup

#웹페이지를 로딩(메서드체인)
page = open("c:\\work\\test01.html", "rt", encoding="utf-8").read()
#검색이 용이한 스프객체생성
soup = BeautifulSoup(page, "html.parser")
#print( soup.prettify() )
#<p>전체 검색
#print( soup.find_all("p") )
#첫번째<p>검색
#print( soup.find("p") )
#검색조건:<p class='outer-text'>
#print( soup.find_all("p", class_="outer-text") )
#<p> attrs => attributes {key:value} dict
#print( soup.find_all("p", attrs={"class":"outer-text"}) )
#id=first 검색 
#print( soup.find_all(id="first") )

#태그의 컨텐츠만 리턴(.text)
for tag in soup.find_all("p"):
    title = tag.text.strip()
    title = title.replace("\n", "")
    print(title)




