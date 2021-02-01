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
        "https://fscalla.en.alibaba.com/product/62501746365-817029715/Modern_Luxury_wooden_coffee_table_with_Stainless_leg_and_TV_cabinet_living_room_table_set.html"
    )
    driver.execute_script(
        "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;"
    )
    time.sleep(2)
    try:
        WebDriverWait(driver, 5).until(
            lambda s: s.find_element_by_class_name("detail-box").is_displayed()
        )
    except TimeoutException:
        print("TimeoutException: Element not found")
        return None
    soup = BeautifulSoup(driver.page_source, "lxml")
    file_name_with_path = (
        "/home/mike/Backup/Program/WebScraper/static/html/testali.html"
    )
    with open(file_name_with_path, mode="w", encoding="utf8") as code:
        code.write(str(soup.prettify()))
    # for link in soup.select('div > div.component-product-list > div > div > div > a'):
    #  linklist.append("https://fscalla.en.alibaba.com"+link.get('href'))


driver = configure_driver()
data = []
getCourses(driver, data)
# close the driver.get
driver.close()
# for linkfile in data:
# print(linkfile)
