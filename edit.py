from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import os
import time

strPath = os.path.realpath(__file__)
nmFolders = strPath.split(os.path.sep)
data = strPath
chromedriver = data.replace(nmFolders[-1], "chromedriver")


def configure_driver():
    # Add additional Options to the webdriver
    chrome_options = Options()
    # add the argument and make the browser Headless.
    chrome_options.add_argument("--headless")
    # Instantiate the Webdriver: Mention the executable path of the webdriver you have downloaded
    # For linux/Mac
    # driver = webdriver.Chrome(options = chrome_options)
    # For windows
    driver = webdriver.Chrome(executable_path=chromedriver, options=chrome_options)
    return driver


def getCourses(driver, linklist):
    # Step 1: Go to pluralsight.com, category section with selected search keyword
    # driver.get("https://fscalla.en.alibaba.com/productgrouplist-817029715-1/TV_Stand.html?spm=a2700.icbuShop.41413.5.2758218aI0AAmu&filterSimilar=true&filter=null&sortType=null")
    # wait for the element to load
    driver.get(
        "https://fscalla.en.alibaba.com/productgrouplist-820627505/Coffee_Table.html?spm=a2700.shop_pl.88.23.7496218a0cjK34"
    )
    driver.execute_script(
        "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;"
    )
    time.sleep(30)
    try:
        WebDriverWait(driver, 5).until(
            lambda s: s.find_element_by_class_name("module-product-list").is_displayed()
        )
    except TimeoutException:
        print("TimeoutException: Element not found")
        return None
    # Step 2: Create a parse tree of page sources after searching
    soup = BeautifulSoup(driver.page_source, "lxml")
    # print(soup["href"])
    for link in soup.find_all("a", class_="product-image"):
        # if link.startswith('/product/'):
        #    linklist.append(link)
        linklist.append("http://fscalla.en.alibaba.com" + link.get("href"))
    print(linklist)
    print(len(linklist))


# create the driver object.
driver = configure_driver()
# search_keyword = "Web Scraping"
data = []
getCourses(driver, data)
# close the driver.
driver.close()
print("driver is close")
import csv

with open("csvfile.csv", "wb") as csv_file:
    for line in data:
        csv_file.write(line.encode())
        csv_file.write("\n".encode())
