import requests
from bs4 import BeautifulSoup

search_keyword = "맥북에어"

url = f"https://search.naver.com/search.naver?sm=tab_hty.top&where=nexsearch&query={search_keyword}"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# posts = soup.find_all('li', {'class':'bx _svp_item'})
#     for post in posts:
#         blog_name = post.find('a', {'class':'sub_txt sub_name'}).text
#         try:
#             blog_address = blog_name['href']
    
blog_posts = soup.find_all('li', {'class':'bx _svp_item'})
for post in blog_posts:
    blog_name = post.find('a', {'class':'sub_txt sub_name'}).text
    blog_address = blog_name['href']
    print(blog_name)
    print(blog_address)
