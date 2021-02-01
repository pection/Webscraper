from bs4 import BeautifulSoup

soup = BeautifulSoup(open("./static/html/testali.html"), "html.parser")

href = soup.find_all()
