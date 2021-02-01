from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import os
import time
import csv

strPath = os.path.realpath(__file__)
nmFolders = strPath.split(os.path.sep)
data = strPath
chromedriver = data.replace(nmFolders[-1], "chromedriver")


def remove_duplicates(original):
    unique = []
    [unique.append(n) for n in original if n not in unique]
    return unique


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
        "https://fscalla.en.alibaba.com/productgrouplist-817029715-1/TV_Stand.htmlandow.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;"
    )
    time.sleep(10)
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
    for link in soup.select("div > div.component-product-list > div > div > div > a"):
        linklist.append([link.get("href")])


#        linklist.append("https://fscalla.en.alibaba.com"+link.get('href'))
#    print (linklist)
#    print (len(linklist))
# create the driver object.
driver = configure_driver()
# search_keyword = "Web Scraping"
data = []
getCourses(driver, data)
# close the driver.get
driver.close()
import csv

file = open("csvfile.csv", "w+", newline="")
with file:
    write = csv.writer(file)
    write.writerows(data)
