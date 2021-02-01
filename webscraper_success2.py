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


def remove_duplicates(original):
    unique = []
    [unique.append(n) for n in original if n not in unique]
    return unique


def configure_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(executable_path=chromedriver, options=chrome_options)
    return driver


def getCourses(driver, linklist):
    driver.get(
        "https://fscalla.en.alibaba.com/productgrouplist-820601440-2/Side_Table.html?spm=a2700.shop_pl.41413.42.22d95cbbb8uaEM&filterSimilar=true&filter=null&sortType=null"
    )
    driver.execute_script(
        "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;"
    )
    time.sleep(30)
    try:
        WebDriverWait(driver, 10).until(
            lambda s: s.find_element_by_class_name("module-product-list").is_displayed()
        )
    except TimeoutException:
        print("TimeoutException: Element not found")
        return None
    soup = BeautifulSoup(driver.page_source, "lxml")
    # file_name_with_path="/home/mike/Backup/Program/WebScraper/static/html/tvstand.html"
    # with open(file_name_with_path, mode="w",  encoding="utf8") as code:
    #    code.write(str(soup.prettify()))
    for link in soup.select("div > div.component-product-list > div > div > div > a"):
        linklist.append("http://fscalla.en.alibaba.com" + link.get("href"))


driver = configure_driver()
data = []
getCourses(driver, data)
# close the driver.get
driver.close()
import csv

with open("Side_Table2.csv", "wb") as csv_file:
    for line in data:
        csv_file.write(line.encode())
        csv_file.write("\n".encode())
