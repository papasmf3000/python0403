import requests
from bs4 import BeautifulSoup

search_keyword = input("Enter search keyword: ")

for i in range(1, 101):
    url = f"https://search.naver.com/search.naver?sm=tab_hty.top&where=nexsearch&query={search_keyword}&start={i*10-9}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    blog_list = soup.find_all('li', class_='bx')

    for blog in blog_list:
        blog_title = blog.find('a', class_='api_txt_lines total_tit').get_text()
        blog_url = blog.find('a', class_='api_txt_lines total_tit')['href']
        blog_date = blog.find('span', class_='sub_time sub_txt').get_text()

        print("Title:", blog_title)
        print("URL:", blog_url)
        print("Date:", blog_date)
        print("="*50)
