import time
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#간혹 셀리니움을 사용하는 경우 부착한 드라이버 오류가 출력되면
#아래와 같이 옵션을 지정해 주면 된다. 
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)

#해당 주소로 네이버스마트스토어에서 저가의 노트북을 검색한다. 
URL = 'https://search.shopping.naver.com/search/all?frm=NVSHATC&origQuery=%EB%85%B8%ED%8A%B8%EB%B6%81&pagingIndex=1&pagingSize=40&productSet=total&query=%EB%85%B8%ED%8A%B8%EB%B6%81&sort=price_asc&timestamp=&viewType=list'

driver.get(URL)

#가격을 검색하는 경우 
#<span class="price_num__S2p_v" data-testid="SEARCH_PRODUCT_PRICE">300,000원</span>

# 스크롤을 해야 데이터가 출력되는 경우라면 약간의 자바스크립트 코드를 실행해야 한다. 
# 처음 브라우저 창의 높이를 구합니다.
# last_height = driver.execute_script("return document.body.scrollHeight")
# count = 0 
# while True:
#     # 가장 아래까지 (창의 높이만큼) 스크롤을 내립니다.
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     # 새로운 내용 로딩될때까지 기다림 (이를 위해 내장 모듈 time을 임포트해야해요)
#     time.sleep(5)
#     # 다시 현재 브라우저의 창의 높이를 구합니다. (페이지가 더 로드됐다면 늘어났겠죠?)
#     new_height = driver.execute_script("return document.body.scrollHeight")
#     # 새로운 창의 높이가 직전의 높이와 같을 때 (더 이상 로드될 컨텐츠가 없을때까지)
#     if new_height == last_height:
#     	break
#     last_height = new_height

soup = BeautifulSoup(driver.page_source, 'html.parser')
#<div class="basicList_item__0T9JD">
#<div class="basicList_title__VfX3c"><a target="_blank" class="basicList_link__JLQJf" rel="noopener" data-nclick="N=a:lst*N.title,i:38275740209,r:1" data-testid="SEARCH_PRODUCT" title="에이수스 BR1100 노트북 11.6인치 HD 안티글레어 디스플레이 180도 Celeron N4500 4GB 64GB SSD MIL-STD 81" href="https://cr.shopping.naver.com/adcr.nhn?x=freLdT9m9WPINtiWd5C4rf%2F%2F%2Fw%3D%3DsVzK1v2kTsNrX681eLMGSl8gdJNsJvWEbjkYl0KjGHwn2JuB1xbdLlYSG9uR1HG3p2m%2FR0oefaMAcZ0IDu7l0XYWa6%2BN5ktvoHFUYfjtkGRN6gjaE1mJLtk9Tc5U4OSQ6JOL2TQoo3DzNZmFEvqmT539jBvQF78L7i7pnL4F1ZjMNaLo85e6Ha77aQ4Q%2Fp7sSCq3iKqLj%2BRWT3kLVMX8TXXTz%2Bfe6hEj9vgfix1uQHGWTobqyvaPhQbxB%2FhxPg5Vh%2FlrTNZE3aK%2FlzAsvb307BKuKWQN4b7WstTXVRp4V%2Fd2Kx7G3krbJiQXzryuwwOqJJ3QdJri6beSK5HOlNjCKdq5ET11%2BboBd8L%2FWQFm7bzvHvY%2FUzN94OzIr5wG3PfiAmeEuhr0Ddhlr9VIE9eSqyJX7lP3BE1QtRX9GLtMXEJOxHP8nqNlC7Bp0kdvoj5zMgjkkRpkF7l6Z4QEsOIx7zPG57q82hY9XwSXCnG3zwHKd1hqbdBXYAqqT6hczQWIZlfFGbF1zbHCdn839R0odPLzClQeC5yhdLl%2FSkM5EEryPzjhR6ryOQe8nNbEIM2q%2B280gu%2FmYImyPWrGxPeogUbB%2FbsZT%2FpCF8YFM28PRHXFrWNLxRrWHCJoudYzHCivGkr4jCIL8x2do773NAwpuJgDPWqZvn22Ian6VKsr6QdZvU2Y6hEEwGxc1AZfON9sL4VRAH%2BsMDObarUodGweR8Q%3D%3D&amp;nvMid=38275740209&amp;catId=50000151">에이수스 BR1100 노트북 11.6인치 HD 안티글레어 디스플레이 180도 Celeron N4500 4GB 64GB SSD MIL-STD 81</a></div>
#<span class="price_num__S2p_v" data-testid="SEARCH_PRODUCT_PRICE">300,000원</span>
count = 0 
goods_list = soup.select('div.basicList_item__0T9JD')
try: 
    for v in goods_list:
        item_name = v.select_one('div.basicList_title__VfX3c > a').get('title')
        item_price = v.select_one('span.price_num__S2p_v').text
        print(item_name)
        print(item_price)
        count += 1 
        print("count:{0}".format(count))
except:
    pass 
