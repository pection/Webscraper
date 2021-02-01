from lxml import html
import requests

page = requests.get(
    "https://fscalla.en.alibaba.com/productgrouplist-820627505/Coffee_Table.html?spm=a2700.shop_pl.88.23.7496218a0cjK34"
)
tree = html.fromstring(page.content)
print(tree)
# This will create a list of buyers:
links = tree.xpath(
    '/html/body/div[2]/div[3]/div[2]/div[2]/div[1]/div/div[1]/form/div/ul/li/div/div[1]/a [contains(@href, "a")]'
)
# This will create a list of prices
img_link = []
for index, link in enumerate(links):
    args = (index, link.xpath("@href").extract(), link.xpath("img/@src").extract())
    print("The link %d pointing to url %s and image %s" % args)
    img_link.append(args)
# print('Buyers: ', buyers)
# print('Prices: ', prices)
print(img_link)
