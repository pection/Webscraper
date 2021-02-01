#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib3
import requests

http = urllib3.PoolManager()
url = "https://subscription.packtpub.com/video/big_data_and_business_intelligence/9781789806892/99073/99215/course-overview"
html_page = requests.get(url)
soup = BeautifulSoup(html_page.content, "html.parser")
print(soup)
