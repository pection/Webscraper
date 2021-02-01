from requests_html import HTMLSession
from bs4 import BeautifulSoup

session = HTMLSession()
resp = session.get(
    "https://fscalla.en.alibaba.com/productgrouplist-817029715-1/TV_Stand.html"
)
count = 0
resp.html.render()
soup = BeautifulSoup(resp.html.html, "lxml")
for link in soup.find_all("a", class_="product-image"):
    if link.text:
        print(link)
    # print (link.get('href'))
    count += 1
